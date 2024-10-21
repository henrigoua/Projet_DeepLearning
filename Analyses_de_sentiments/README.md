
# Analyse de Sentiment avec Deep Learning

## Description

Ce projet vise à réaliser une analyse de sentiment sur des données textuelles à l'aide d'un modèle de deep learning. L'objectif est de classifier un texte en différentes catégories de sentiment, telles que **Positif**, **Négatif** ou **Neutre**. Le modèle utilise une combinaison de réseaux de neurones convolutifs (CNN) et de couches LSTM pour capturer à la fois les caractéristiques locales et les dépendances à long terme dans le texte d'entrée.

L'analyse de sentiment est un outil puissant pour comprendre l'opinion publique et l'émotion derrière des textes, tels que les avis clients ou les discussions sur les réseaux sociaux. Ce projet vise à classer automatiquement les sentiments exprimés dans un texte en utilisant des techniques avancées de deep learning.

## Objectifs du Projet

- **Classification de Sentiment** : Développer un modèle capable de prédire avec précision le sentiment d'un texte.
- **Approche par Deep Learning** : Utiliser un réseau de neurones séquentiel combinant des couches CNN, LSTM, et entièrement connectées pour une classification efficace des sentiments.
- **Recherche d'Hyperparamètres** : Explorer plusieurs hyperparamètres pour optimiser les performances du modèle, y compris le taux d'apprentissage, la taille des lots, et le nombre d'époques.
- **Évaluation du Modèle** : Évaluer les performances du modèle en utilisant des métriques clés telles que l'exactitude, la précision, le rappel et la perte de validation.

## Jeu de Données

Le projet utilise le **Twitter Airline Sentiment Dataset** disponible sur Kaggle, qui contient des tweets classés en **positif**, **négatif**, ou **neutre** à propos de compagnies aériennes. Cependant, tout jeu de données étiqueté pour l'analyse de sentiment (par exemple, les avis de films IMDb, les avis Yelp, ou des jeux de données personnalisés) peut être utilisé.

### Détails du Dataset

- **Source** : [Twitter Airline Sentiment Dataset](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)
- **Échantillons** : 14,640 tweets
- **Colonnes clés** : `tweet_id`, `airline_sentiment`, `airline`, `text`

Le dataset est divisé en un ensemble d'entraînement et un ensemble de test pour entraîner et évaluer le modèle.


## Améliorations Futures

- **Transformers pour une meilleure compréhension contextuelle** : Des modèles basés sur des architectures de transformateurs, comme BERT, ont montré des performances exceptionnelles pour la classification de textes en raison de leur capacité à comprendre le contexte plus profondément.
- **Jeux de Données Plus Grands** : Étendre le jeu de données pour inclure une plus grande variété de textes et de sentiments afin d'améliorer la généralisation du modèle à travers différents types de texte.
- **Augmentation de données** : Utiliser des techniques d'augmentation de texte pour enrichir les données d'entraînement, ce qui peut aider à généraliser le modèle à de nouveaux types de textes.
- **Déploiement du Modèle** : Créer une interface utilisateur (UI) ou déployer le modèle dans un environnement cloud pour une analyse des sentiments en temps réel.

## Comment Exécuter le Projet

1. **Installer les dépendances** :
   Assurez-vous que toutes les bibliothèques sont installées en exécutant la commande suivante :
   ```bash
   pip install -r requirements.txt
   ```

2. **Télécharger le dataset** :
   Téléchargez le dataset depuis Kaggle et placez-le dans le répertoire `data/` :
   ```bash
   kaggle datasets download -d crowdflower/twitter-airline-sentiment
   ```

3. **Lancer l'entraînement** :
   Exécutez le notebook `analyse_sentiment.ipynb` pour lancer l'entraînement du modèle.

4. **Évaluer le Modèle** : Après l'entraînement, évaluer les performances du modèle à l'aide du jeu de test.

## Conclusion

Ce projet démontre l'utilisation de techniques de deep learning, en particulier une combinaison de CNN et LSTM, pour l'analyse de sentiment. En ajustant les hyperparamètres et en utilisant des techniques d'entraînement efficaces, le modèle est capable de prédire le sentiment d'un texte avec un haut degré de précision.

## License

This project is licensed under the MIT License.

