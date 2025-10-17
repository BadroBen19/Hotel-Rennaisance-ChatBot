import streamlit as st
import time
from query_data import query_rag

# Configuration de la page
st.set_page_config(
    page_title="Hôtel Renaissance Tlemcen",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS simplifié
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Background global */
    .stApp {
        background-color: #FEFEFE;
        font-family: 'Inter', sans-serif;
    }
    
    /* Titre principal */
    .main-title {
        text-align: center;
        color: #000000 !important;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        margin-top: 2rem;
    }
    
    /* Container principal */
    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #E8E8E8;
        margin-top: 2rem;
    }
    
    /* Input styling - corrigé */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #E8E8E8;
        padding: 12px 16px;
        font-size: 16px;
        background-color: white;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #2E86AB;
        box-shadow: 0 0 0 2px rgba(46, 134, 171, 0.1);
        outline: none;
    }
    
    /* Boutons simples */
    .stButton > button {
        width: 100%;
        background-color: #2E86AB;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #1E5F80;
        transform: translateY(-1px);
    }
    
    /* Réponse styling */
    .response-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        border-left: 4px solid #2E86AB;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .response-text {
        font-size: 16px;
        line-height: 1.6;
        color: #2C3E50;
        margin-bottom: 10px;
    }
    
    .sources-text {
        font-size: 12px;
        color: #666;
        font-style: italic;
    }
    
    /* Footer simple */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 2rem;
        color: #666;
        font-size: 14px;
        border-top: 1px solid #E8E8E8;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        .main-container {
            margin: 1rem;
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Interface principale
def main():
    # Titre simple en noir
    st.markdown('<h1 class="main-title">Hôtel Renaissance Tlemcen</h1>', unsafe_allow_html=True)
    
    # Container principal
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        # Zone de saisie
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            question = st.text_input(
                "",
                placeholder="Tapez votre question ici...",
                help="Posez une question sur l'hôtel",
                label_visibility="collapsed"
            )
        
        # Bouton de recherche centré
        col1, col2, col3 = st.columns([3, 2, 3])
        with col2:
            search_button = st.button("Rechercher", type="primary")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Traitement de la requête
    if search_button and question:
        with st.container():
            with st.spinner("Recherche en cours..."):
                start_time = time.time()
                try:
                    response = query_rag(question)
                    processing_time = time.time() - start_time
                    
                    # Affichage de la réponse
                    st.markdown(
                        f"""
                        <div class="response-container">
                            <h3 style="color: #2E86AB; margin-bottom: 15px;">Réponse</h3>
                            <div class="response-text"><strong>{response}</strong></div>
                            <div class="sources-text">Réponse générée en {processing_time:.1f} secondes</div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                    
                except Exception as e:
                    st.error(f"Erreur lors de la recherche : {str(e)}")
    
    elif search_button and not question:
        st.warning("Veuillez saisir une question.")
    
    # Sidebar avec exemples
    with st.sidebar:
        st.markdown("### Questions d'exemple")
        
        examples = [
            "Les animaux de compagnie sont-ils autorisés ?",
            "À quelle heure puis-je m'enregistrer ?",
            "Quels sont les services disponibles ?",
            "Où se trouve l'hôtel ?",
            "Comment puis-je vous contacter ?",
            "Y a-t-il un restaurant ?",
            "Le parking est-il gratuit ?"
        ]
        
        for i, example in enumerate(examples):
            if st.button(example, key=f"example_{i}"):
                # Utiliser session state pour passer la question
                st.session_state.selected_question = example
                st.experimental_rerun()
    
    # Gérer la question sélectionnée depuis la sidebar
    if 'selected_question' in st.session_state:
        question = st.session_state.selected_question
        del st.session_state.selected_question
        # Auto-déclencher la recherche
        with st.spinner("Recherche en cours..."):
            start_time = time.time()
            try:
                response = query_rag(question)
                processing_time = time.time() - start_time
                
                st.markdown(
                    f"""
                    <div class="response-container">
                        <h3 style="color: #2E86AB; margin-bottom: 15px;">Réponse</h3>
                        <div class="response-text"><strong>{response}</strong></div>
                        <div class="sources-text">Réponse générée en {processing_time:.1f} secondes</div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
            except Exception as e:
                st.error(f"Erreur lors de la recherche : {str(e)}")
    
    # Footer simple
    st.markdown(
        """
        <div class="footer">
            <p><strong>Propulsé par</strong> Intelligence Artificielle</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()