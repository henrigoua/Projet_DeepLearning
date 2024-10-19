
# Projet de Détection de Marque de Voiture

## Description
Ce projet utilise le deep learning pour identifier les marques et modèles de voitures à partir d'images téléchargées par les utilisateurs. Il est composé d'une API backend développée avec FastAPI pour gérer les requêtes de prédiction et d'une interface utilisateur Streamlit qui permet le téléchargement d'images et l'affichage des résultats de prédiction.

## Fonctionnalités
- **Prédiction de marque et modèle** : Les utilisateurs peuvent télécharger des images de voitures et obtenir des prédictions précises sur la marque et le modèle.
- **Interface utilisateur interactive** : Une interface facile à utiliser construite avec Streamlit pour une expérience utilisateur optimale.
- **API robuste** : Un backend FastAPI garantit des réponses rapides et fiables pour les requêtes de prédiction.

## Technologies Utilisées
- **Python** : Langage de programmation principal.
- **FastAPI** : Framework pour construire des APIs de haute performance.
- **Streamlit** : Framework pour créer des applications de data science.
- **TensorFlow/Keras** : Utilisé pour le développement et l'entraînement des modèles de machine learning.
- **Pillow** : Bibliothèque pour le traitement d'images en Python.

## Structure du Projet
```
DETECTION_VOITURE/
│
├── app/
│   ├── backend.py    # Backend API
│   ├── frontend.py   # Interface utilisateur Streamlit
│
├── model/
│   ├── model.h5       # Modèle de machine learning pré-entraîné
│
├── car_brand_detection_Dataset/
│
├── Detection_voiture.ipynb  # Jupyter notebook pour les démonstrations
│
├── logs/  # Dossiers pour les logs
│
├── requirements.txt  # Fichier pour les dépendances Python
├── README.md  # Guide et informations du projet
└── .gitignore  # Fichier pour ignorer les fichiers non nécessaires dans git
```

## Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Dépendances
Installez les dépendances du projet en exécutant :
```bash
pip install -r requirements.txt
```

## Utilisation

### Lancer le serveur FastAPI
Pour démarrer le serveur backend, naviguez dans le dossier `app` et exécutez :
```bash
uvicorn backend:app --reload 
```

### Lancer l'interface Streamlit
Pour démarrer l'interface utilisateur, naviguez dans le dossier `app` et exécutez :
```bash
streamlit run frontend.py
```

## Contribuer
Les contributions sont toujours les bienvenues. Veuillez explorer les issues ouvertes ou soumettre un pull request si vous souhaitez proposer des améliorations ou des corrections.

## Licence
Ce projet est distribué sous la licence [Nom de la Licence], ce qui permet une utilisation, une modification et une distribution libre.


## Contact
Pour plus d'informations, contactez [Goua Beedi](mailto:gouabeedi@gmail.com).

