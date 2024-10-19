import streamlit as st
import requests
from PIL import Image
import io

# Styles CSS pour améliorer l'apparence des onglets et du contenu
# Styles CSS pour améliorer l'apparence des onglets et du contenu
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        font-weight:bold;
        color: #4CAF50; /* Couleur verte pour une emphase positive */
    }
    .image-upload {
        margin: 10px 0;
        padding: 10px;
        border: 2px solid #0066CC; /* Bleu vif pour améliorer la visibilité */
        border-radius: 5px;
        background-color: #f0f0f0; /* Couleur de fond plus douce pour l'œil */
    }
    .stButton>button {
        color: #fff;
        background-color: #0066CC;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Configuration du titre de la page
st.title('Prédiction de Marque de Voiture')

# Configuration de la barre latérale pour les paramètres ou les instructions
st.sidebar.header("Paramètres de l'Image")
uploaded_file = st.sidebar.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"], help="Téléchargez une image de voiture ici.")

# Utilisation de st.tabs pour ajouter des onglets
tabs = st.tabs(["🚗 Prédiction", "ℹ️ À propos"])

# Onglet de prédiction
with tabs[0]:
    st.markdown("""
    <div style='font-size:16px;'>Ce prototype permet de prédire la marque d'une voiture à partir d’une image. Veuillez télécharger une image de voiture ci-dessous et le modèle prédira sa marque et son modèle.</div>
    """, unsafe_allow_html=True)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # Convertir l'image en RGB si nécessaire
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        st.image(image, caption='Image téléchargée', use_column_width=True)
        st.markdown('<p class="big-font">Classifying...</p>', unsafe_allow_html=True)

        # Préparation des données de l'image pour l'envoi par requête POST
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        byte_data = buffer.getvalue()

        # Envoi de la requête POST à l'API FastAPI
        url = 'http://127.0.0.1:8000/predict'  # Utilisation de l'adresse IP explicite
        files = {'file': ('image.jpeg', byte_data, 'image/jpeg')}
        
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                prediction = response.json()
                st.markdown('### Résultats de la prédiction :', unsafe_allow_html=True)
                st.markdown(f"**Marque de voiture prédite :** {prediction['class']}", unsafe_allow_html=True)
                st.markdown(f"**Confiance dans la prédiction :** {prediction['confidence']:.2f}%", unsafe_allow_html=True)
            elif response.status_code == 400:
                st.error("La demande a échoué : les données envoyées sont incorrectes. Vérifiez l'image soumise.")
            elif response.status_code == 500:
                st.error("Erreur interne du serveur. Veuillez réessayer plus tard ou contacter le support technique.")
            else:
                st.error(f"Échec de la prédiction avec le statut HTTP : {response.status_code}. Veuillez réessayer.")
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion avec le serveur : {str(e)}. Veuillez vérifier votre connexion réseau ou l'état du serveur.")

# Onglet À propos
with tabs[1]:
    st.subheader("À propos de cette application")

    # Amélioration du style avec HTML
    st.markdown("""
    <style>
        .about-text {
            font-size:16px;
            line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    # Texte enrichi pour une meilleure compréhension et présentation
    st.markdown("""
    <div class="about-text">
        <p>Cette application démontre l'utilisation pratique des technologies de deep learning pour reconnaître les marques de voitures à partir de photographies. Elle est destinée à aider les passionnés d'automobile ainsi que les professionnels du secteur à identifier rapidement des modèles de voitures.</p>
        <p>Le moteur de prédiction repose sur un modèle de convolution neural network (CNN), entraîné sur une large base de données contenant des milliers d'images de voitures classées par marque et modèle. Ce modèle a été optimisé pour offrir à la fois précision et rapidité, fournissant des prédictions en quelques secondes.</p>
        <p><strong>Comment utiliser cette application ?</strong><br>
        Téléchargez une image de voiture via le menu de gauche, et le système analysera l'image pour prédire la marque et le modèle du véhicule. Les résultats incluront la marque prédite ainsi qu'un indice de confiance associé à cette prédiction.</p>
        <p>Ce projet a été développé en utilisant Python, avec Streamlit pour l'interface utilisateur et FastAPI pour gérer les requêtes backend. Les images sont traitées en temps réel, démontrant ainsi la capacité du modèle à être intégré dans des applications en ligne.</p>
    </div>
    """, unsafe_allow_html=True)

