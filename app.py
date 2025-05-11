from fastapi import FastAPI
import joblib
import pandas as pd
from app.schemas import ShipmentData, Prediction

app = FastAPI()
model = joblib.load("app/model.pkl")

@app.post("/predict", response_model=Prediction)
def predict(data: ShipmentData):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {"on_time": bool(prediction)}
