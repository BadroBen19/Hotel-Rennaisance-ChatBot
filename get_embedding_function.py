from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_function():
    model_name ="sentence-transformers/all-mpnet-base-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings