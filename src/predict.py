import joblib
from src.preprocessing import preprocess

model = joblib.load("models/noshow_model.pkl")
