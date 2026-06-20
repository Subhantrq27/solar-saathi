# ☀️ Solar Saathi — Pakistan's AI-Powered Solar Advisor

> A mobile app that helps Pakistani homeowners decide the right solar system for their home — in Urdu and English.

---

## 📱 What is Solar Saathi?

Solar panels are everywhere in Pakistan. But most people don't know:
- How many panels do they need?
- How much will they save per month?
- When will the investment pay back?

**Solar Saathi** answers all of this in seconds using a trained ML model.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🧮 AI Calculator | Enter city, monthly units, roof size → get full solar plan |
| 📖 Solar Guide | System costs, brands, On-Grid vs Off-Grid explained |
| 🗺️ Dealer Finder | Nearby solar dealers with one-tap call button |
| 🌐 Bilingual | Full Urdu + English support |
| 📱 Android APK | No Expo Go needed — install directly |

---

## 🤖 How Does the AI Work?

A **Random Forest Regressor** trained on Pakistani city data:

**Input Features:**
- Monthly electricity units (from bill)
- Roof size (square feet)
- WAPDA tariff (Rs per unit)
- City sun hours (NASA POWER data)

**Predictions:**
- Panels needed
- System size (kW)
- Monthly saving (Rs)
- Payback time (years)

**Key logic:**
- More sun hours (Karachi/Quetta) → fewer panels needed
- Higher tariff → more savings → faster payback
- Bigger roof + more units → larger system

---

## 🏗️ Architecture

```
📱 React Native App (Android)
        ↓ HTTPS
🚀 FastAPI Backend (Railway)
        ↓
🤖 Random Forest Model (.pkl)
        ↓
📊 Result → back to app
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Mobile App | React Native + Expo (SDK 56) |
| Backend | FastAPI + Uvicorn |
| ML Model | scikit-learn Random Forest |
| Database | — (stateless, no DB needed) |
| Deployment | Railway (backend) + EAS Build (APK) |
| Language | Python + TypeScript |

---

## 📂 Project Structure

```
solar-saathi/
├── backend/
│   ├── main.py              # FastAPI app
│   ├── solar_model.pkl      # Trained ML model
│   ├── requirements.txt
│   └── Dockerfile
├── ml_model/
│   ├── train_model.py       # Model training script
│   └── pakistan_solar_data.csv
└── mobile/
    └── src/app/
        └── index.tsx        # Main React Native app
```

---

## ⚙️ Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Mobile
```bash
cd mobile
npm install
npx expo start
```

### Train Model
```bash
cd ml_model
python train_model.py
```

---

## 🌍 Live

- **Backend API:** https://solar-saathi-production.up.railway.app
- **API Docs:** https://solar-saathi-production.up.railway.app/docs
- **Android APK:** [Download here](https://expo.dev/accounts/subhantrq/projects/mobile/builds/29d9916b-1ac2-4e3b-8c07-e3c4951fa6a1)

---

## 🗺️ Cities Supported

Lahore · Karachi · Islamabad · Peshawar · Multan · Quetta · Faisalabad · Rawalpindi · Hyderabad · Attock

---

## 🔮 What's Next

- [ ] Larger dataset with real NEPRA data
- [ ] Net metering calculator
- [ ] Real dealer database with reviews
- [ ] iOS support
- [ ] Loadshedding schedule per city

---

## 👨‍💻 Built By

**Muhammad Subhan Tariq**
Final-year CS student @ FAST-NUCES Peshawar
AI/ML Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/subhan-tariq-b57aa225b)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/Subhantrq27)

---

## 📄 License

MIT License — free to use, improve, and share.

---

> *Built in response to a real problem — because every Pakistani deserves to make an informed solar decision.* 🇵🇰
