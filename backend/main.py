from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Solar Saathi API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("solar_model.pkl")

CITY_SUN_HOURS = {
    "Lahore": 5.2, "Karachi": 6.1, "Islamabad": 5.5,
    "Peshawar": 5.8, "Multan": 6.3, "Quetta": 6.5,
    "Faisalabad": 5.4, "Rawalpindi": 5.3, "Hyderabad": 6.0,
    "Attock": 5.6
}

class SolarInput(BaseModel):
    city: str
    monthly_units: float
    roof_sqft: float
    wapda_tariff_pkr: float

@app.get("/")
def root():
    return {"message": "Solar Saathi API chal rahi hai!"}

@app.post("/predict")
def predict(data: SolarInput):
    sun_hours = CITY_SUN_HOURS.get(data.city, 5.5)
    features = np.array([[
        data.monthly_units,
        data.roof_sqft,
        data.wapda_tariff_pkr,
        sun_hours
    ]])
    prediction = model.predict(features)[0]
    return {
        "city": data.city,
        "panels_needed": round(prediction[0]),
        "system_kw": round(prediction[1], 1),
        "monthly_saving_pkr": round(prediction[2]),
        "payback_years": round(prediction[3], 1),
        "sun_hours_per_day": sun_hours
    }
