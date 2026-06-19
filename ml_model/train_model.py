import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

df = pd.read_csv("pakistan_solar_data.csv")

features = ["monthly_units", "roof_sqft", "wapda_tariff_pkr", "sun_hours_per_day"]
targets = ["panels_needed", "system_kw", "monthly_saving_pkr", "payback_years"]

X = df[features]
y = df[targets]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model trained! MAE: {mae:.2f}")

joblib.dump(model, "solar_model.pkl")
print("Model saved: solar_model.pkl")
