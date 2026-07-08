from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="House Price Prediction API")

# Load trained model
model = joblib.load("final_model.pkl")


class HouseData(BaseModel):
    OverallQual: float
    GrLivArea: float
    GarageCars: float
    GarageArea: float
    TotalBsmtSF: float
    FirstFlrSF: float
    FullBath: float
    TotRmsAbvGrd: float
    YearBuilt: float
    YearRemodAdd: float


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is Running!"
    }


@app.post("/predict")
def predict(data: HouseData):

    input_df = pd.DataFrame({
        "OverallQual": [data.OverallQual],
        "GrLivArea": [data.GrLivArea],
        "GarageCars": [data.GarageCars],
        "GarageArea": [data.GarageArea],
        "TotalBsmtSF": [data.TotalBsmtSF],
        "1stFlrSF": [data.FirstFlrSF],
        "FullBath": [data.FullBath],
        "TotRmsAbvGrd": [data.TotRmsAbvGrd],
        "YearBuilt": [data.YearBuilt],
        "YearRemodAdd": [data.YearRemodAdd],
    })

    prediction = model.predict(input_df)

    return {
        "Predicted House Price": round(float(prediction[0]),2)
    }