# 🏥 Medication Reconciliation System

## 📌 Overview
This project is a FastAPI-based backend system for managing patient medication data from multiple sources and detecting conflicts.

It supports:
- Multi-source medication ingestion
- Conflict detection across sources
- Versioned medication snapshots
- Conflict resolution tracking
- Aggregation and reporting

---

## 🚀 Features

### 🔹 Ingestion
- Accept medication data from:
  - clinic_emr
  - hospital_discharge
  - patient_reported

### 🔹 Normalization
- Converts medication names to lowercase
- Ensures consistent structure

### 🔹 Conflict Detection
Detects:
- Dose mismatch (same drug, different dose)
- Status conflict (active vs inactive)
- Drug interaction (based on predefined rules)

### 🔹 Versioning
- Each ingestion creates a new snapshot version
- Maintains longitudinal history

### 🔹 Conflict Resolution
- Mark conflicts as resolved
- Store reason and timestamp

### 🔹 Reporting
- Patients with unresolved conflicts per clinic
- Patients with ≥ 2 conflicts in last 30 days

---

## 🛠 Tech Stack
- FastAPI
- MongoDB Atlas
- PyMongo
- Pytest

---

## 📂 Project Structure

med_reconciliation/
│
├── app/
│   ├── routes/
│   │   ├── ingestion.py
│   │   └── reports.py
│   ├── services/
│   │   ├── conflict_detection.py
│   │   ├── normalization.py
│   │   └── rules.py
│   ├── db.py
│   └── schemas.py
│
├── tests/
│   ├── test_conflicts.py
│   └── test_reports.py
│
├── seed/
│   └── seed_data.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Setup

Clone repo:
git clone <your-repo-link>
cd med_reconciliation

Create venv:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

---

## ⚙️ MongoDB Setup

Update in app/db.py:
MongoClient("your_mongodb_connection_string")

---

## ▶️ Run Application

uvicorn app.main:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

---

## 🌱 Seed Data

python seed/seed_data.py

---

## 🧪 Run Tests

PYTHONPATH=. pytest

---

## 📊 API Endpoints

POST /patients/{patient_id}/medications  
GET /report/clinic/{clinic_name}  
GET /report/conflicts/summary  
POST /conflicts/{conflict_id}/resolve  

---

## 🗃 MongoDB Data Model

Snapshots:
- patient_id
- version
- timestamp
- sources

Conflicts:
- type
- medication(s)
- details
- resolved
- resolution
- patient_id
- timestamp

---

## ⚖️ Design Decisions

- Denormalized schema for faster reads
- Snapshot-based versioning
- Static rule-based conflict detection
- Conflict recalculated after each ingestion

---

## ⚠️ Notes

- Replace MongoDB URI before running
- Handles malformed input safely
- Uses UTC timestamps

---

## 📈 Future Improvements

- Real drug database integration
- Better resolution logic
- Authentication
- Frontend UI

---

## 👨‍💻 Author

Arjun Manohar  
B.Tech CSE, NIT Calicut
