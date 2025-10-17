import argparse
import os
import time
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Start timer
    start_time = time.time()
    
    # Prepare the DB.
    db_start = time.time()
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    db_time = time.time() - db_start

    # Search the DB.
    search_start = time.time()
    results = db.similarity_search_with_score(query_text, k=5)
    search_time = time.time() - search_start

    # Prepare context and prompt
    prompt_start = time.time()
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    prompt_time = time.time() - prompt_start

    # Generate response
    generation_start = time.time()
    model = Ollama(model="gemma3:1b")
    response_text = model.invoke(prompt)
    generation_time = time.time() - generation_start

    # Calculate total time
    total_time = time.time() - start_time

    # Prepare sources
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    
    # Display results with timing
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    print("\n" + "="*50)
    print("⏱️  TIMING BREAKDOWN:")
    print(f"   📚 Database loading: {db_time:.2f}s")
    print(f"   🔍 Document search:  {search_time:.2f}s")
    print(f"   📝 Prompt creation:  {prompt_time:.2f}s")
    print(f"   🤖 Response generation: {generation_time:.2f}s")
    print(f"   ⚡ TOTAL TIME: {total_time:.2f}s")
    print("="*50)
    
    return response_text


if __name__ == "__main__":
    main()
