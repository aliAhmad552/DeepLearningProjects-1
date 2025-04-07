# Potato Disease Classification

This project is a **Potato Disease Classification System** using deep learning. It includes a machine learning model trained to classify potato diseases, an API built with FastAPI, and a React.js frontend for user interaction.

## Project Structure
```
📂 Potato Disease Classification
│── 📂 api                 # FastAPI Backend
│    ├── main.py           # FastAPI main file
│    ├── requirements.txt  # Dependencies for API
│── 📂 saved_models        # Directory to store trained models
│── 📂 training            # Training scripts and dataset
│    ├── training.ipynb    # Jupyter Notebook for model training
│    ├── model.h5          # Trained deep learning model
│── 📂 frontend            # React.js frontend application
│── README.md              # Project Documentation
```

## Features
```
- Deep Learning Model: Trained using TensorFlow/Keras for potato disease classification.
- FastAPI Backend: API to serve model predictions.
- React Frontend: Web application for user interaction and image uploads.
```

## Setup Instructions
```
1. Clone the Repository
```
```sh
git clone https://github.com/your-repo-name/potato-disease-classification.git
cd potato-disease-classification
```
```
2. Backend Setup (FastAPI)
```
```sh
cd api
pip install -r requirements.txt
```
```sh
uvicorn main:app --reload
```
```
3. Frontend Setup (React)
```
```sh
cd frontend
npm install
```
```sh
npm start
```

## Usage
```
1. Start the FastAPI backend.
2. Start the React frontend.
3. Upload an image of a potato leaf to classify the disease.
4. View the classification result on the UI.
```

## Model Training
```
To train or retrain the model, open `training/training.ipynb` and execute the notebook step by step.
```

## Technologies Used
```
- TensorFlow/Keras: For deep learning model training
- FastAPI: Backend API for model inference
- React.js: Frontend for user interaction
- Uvicorn: ASGI server for FastAPI
```

## Contribution
```
Feel free to contribute by improving the model, API, or frontend. Fork the repository and create a pull request.
```

## License
```
This project is licensed under the MIT License.
```

---
```
Developed by Ali Ahmad 🚀
```
