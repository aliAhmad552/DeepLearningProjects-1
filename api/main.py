import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.saved_model.load("D:\\AI_ML_Projects\\DL_Projects\\Potato_Desease_Recognition\\saved_models\\1")


CLASS_NAMES = ['Early_Blight', 'Late_Blight', 'Healthy']
def read_file_as_image(data) -> np.ndarray:
    try:
        image = Image.open(BytesIO(data)).convert("RGB")  # Ensure RGB format
        image = image.resize((256, 256))  # Resize if needed
        return np.array(image)
    except Exception as e:
        return None  # Handle errors gracefully
# Define a function for prediction
def predict_image(image):
    infer = MODEL.signatures["serving_default"]
    prediction = infer(tf.constant(image))['output_0'].numpy()
    return prediction

@app.get("/ping")
async def ping():
    return {"message": "Server is running"}

@app.post("/predict")
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file is None:
        return {"error": "No file received"}

    print(f"Received file: {file.filename}")  # Debugging print statement

    image = read_file_as_image(await file.read())
    batch_image = np.expand_dims(image, 0)
    batch_image = batch_image.astype('float32')

    prediction = predict_image(batch_image)
    image_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = round(100 * np.max(prediction[0]), 2)

    return {
        'class': image_class,
        'confidence': confidence
    }


if __name__ == "__main__":
    uvicorn.run(app,port=8000, host = 'localhost')