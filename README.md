# 🏨 Hôtel Renaissance Tlemcen - RAG Chatbot

Un système de chatbot intelligent utilisant la technologie RAG (Retrieval-Augmented Generation) pour répondre aux questions sur l'Hôtel Renaissance Tlemcen.

## 🚀 Technologies Utilisées

- **Python 3.x** - Langage principal
- **Streamlit** - Interface web interactive
- **ChromaDB** - Base de données vectorielle
- **Embeddings** - Modèles de vectorisation de texte
- **RAG (Retrieval-Augmented Generation)** - Architecture de recherche et génération

## 📁 Structure du Projet

```
├── app.py                      # Application Streamlit principale
├── get_embedding_function.py   # Configuration des embeddings
├── populate_database.py        # Script de population de la DB
├── query_data.py              # Logique de requête RAG
├── test_rag.py                # Tests du système
├── requirements.txt           # Dépendances Python
├── data/                      # Documents source
└── chroma/                    # Base de données ChromaDB
```

## 🛠️ Installation

1. **Cloner le repository**
```bash
git clone <repository-url>
cd HotelRennaisanceRaG
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Populer la base de données**
```bash
python populate_database.py
```

## 🎯 Utilisation

### Lancer l'application web
```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

### Tester le système
```bash
python test_rag.py
```

### Requête directe
```bash
python query_data.py
```

## ✨ Fonctionnalités

- **Interface moderne** avec design responsive
- **Questions prédéfinies** dans la sidebar
- **Recherche en temps réel** avec indicateur de performance
- **Réponses contextuelles** basées sur les documents de l'hôtel
- **Architecture RAG** pour des réponses précises et pertinentes

## 🎨 Interface

L'application propose :
- Design épuré avec palette de couleurs professionnelle
- Zone de saisie intuitive
- Exemples de questions dans la barre latérale
- Affichage des temps de réponse
- Style responsive pour mobile et desktop

## 📊 Exemples de Questions

- "Les animaux de compagnie sont-ils autorisés ?"
- "À quelle heure puis-je m'enregistrer ?"
- "Quels sont les services disponibles ?"
- "Où se trouve l'hôtel ?"
- "Y a-t-il un restaurant ?"

## 🔧 Configuration

- **Documents** : Placez vos fichiers dans le dossier [`data/`](data/)
- **Embeddings** : Configurez dans [`get_embedding_function.py`](get_embedding_function.py)
- **Base de données** : ChromaDB stockée dans [`chroma/`](chroma/)

## 🧪 Tests

Le système inclut une suite de tests complète dans [`test_rag.py`](test_rag.py) pour vérifier le bon fonctionnement du RAG.

## 📝 Développement

Pour modifier l'interface utilisateur, éditez [`app.py`](app.py). Le CSS est intégré pour un style moderne et responsive.

**Développé avec ❤️ pour l'Hôtel Renaissance Tlemcen**

