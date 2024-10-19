from fastapi import FastAPI, UploadFile
from tensorflow.keras.models import load_model
import numpy as np
import io
from PIL import Image

app = FastAPI()

# Charger le modèle au démarrage de l'application
#model = load_model("../model/model.h5", compile=False)
model = load_model("../model.h5", compile=False)

# Liste des noms de classes prédites par le modèle
CLASS_NAMES = ['hyundai',
 'lexus',
 'mazda',
 'mercedes',
 'opel',
 'skoda',
 'toyota',
 'volkswagen']

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Fonction de prétraitement de l'image
def preprocess_image(image_data):
    try:
        img = Image.open(io.BytesIO(image_data))
        img = img.resize((224, 224))  # Taille requise par la plupart des modèles pré-entraînés
        img = np.asarray(img) / 255.0  # Convertir en tableau numpy et normaliser
        img = np.expand_dims(img, axis=0)  # Ajouter une dimension pour le lot
        return img
    except Exception as e:
        raise ValueError("Erreur dans le prétraitement de l'image : {}".format(e))


    
@app.post("/predict")
async def predict(file: UploadFile):
    try:
        image_data = await file.read()  # Lire les données du fichier
        processed_image = preprocess_image(image_data)  # Prétraiter l'image
        # Faire la prédiction
        predictions = model.predict(processed_image)
        predicted_index = np.argmax(predictions)  # Trouver l'indice de la prédiction maximale
        predicted_class = CLASS_NAMES[predicted_index]  # Trouver la classe correspondante
        confidence = float(np.max(predictions)) * 100  # Calculer la confiance et convertir en pourcentage

        return {
            "class": predicted_class,
            "confidence": round(confidence, 2)
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Erreur lors de la prédiction : {}".format(e)})
