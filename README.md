# 🏥 Medication Reconciliation System

## 📌 Overview
The Medication Reconciliation System is a FastAPI-based backend service designed to ingest, normalize, and reconcile patient medication data from multiple heterogeneous sources.

It detects inconsistencies across sources, maintains versioned medication history, and provides reporting capabilities for clinical analysis.

---

## 🎯 Objectives
- Integrate multi-source medication data
- Normalize heterogeneous inputs
- Detect conflicts across sources
- Maintain longitudinal history
- Provide reporting endpoints

---

## 🚀 Features

### 🔹 Multi-Source Ingestion
Supports ingestion from:
- clinic_emr
- hospital_discharge
- patient_reported

Each ingestion creates a new versioned snapshot, preserving history.

---

### 🔹 Data Normalization
- Converts medication names to lowercase
- Standardizes input structure
- Handles missing/malformed data gracefully

---

### 🔹 Conflict Detection Engine

#### ✅ Dose Mismatch
Same medication appearing with different doses across sources.

#### ✅ Status Conflict
Medication marked as active in one source and inactive in another.

#### ✅ Drug Interaction
Detected using rule-based drug class mappings.

---

### 🔹 Versioning & History
- Snapshot-based versioning
- Each ingestion creates a new version
- Enables tracking of medication changes over time

---

### 🔹 Conflict Resolution
- Conflicts can be marked as resolved
- Stores:
  - resolution reason
  - timestamp
- Maintains auditability

---

### 🔹 Reporting APIs

Patients with unresolved conflicts:
GET /report/clinic/{clinic_name}

Conflict summary (last 30 days):
GET /report/conflicts/summary

Resolve a conflict:
POST /conflicts/{conflict_id}/resolve

---

## 🏗 System Architecture

Client (Swagger UI)  
↓  
FastAPI Backend  
↓  
Services Layer  
- Normalization  
- Conflict Detection  
- Rules Engine  
↓  
MongoDB Atlas  

---

## 🗃 Data Model

### Snapshots Collection
- patient_id  
- version  
- timestamp  
- sources  

Each snapshot stores medications grouped by source.

---

### Conflicts Collection
- type  
- medication(s)  
- details  
- resolved  
- resolution  
- patient_id  
- timestamp  

Stores detected conflicts in an auditable structure.

---

## ⚙️ Technology Stack
- FastAPI  
- MongoDB Atlas  
- PyMongo  
- Pytest  

---

## ⚙️ Setup Instructions

git clone https://github.com/arjun755980/medication-reconciliation-system.git  
cd med_reconciliation  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

Update MongoDB connection string in:
app/db.py

---

## ▶️ Running the Application

uvicorn app.main:app --reload  

Swagger UI:
http://127.0.0.1:8000/docs

---

## 🌱 Seed Data

python seed/seed_data.py  

Generates synthetic patients and conflict scenarios.

---

## 🧪 Testing

PYTHONPATH=. pytest  

Covers:
- Conflict detection logic
- Edge cases (missing fields)
- Aggregation queries

---

## ⚖️ Design Decisions & Trade-offs

Denormalization vs References:
Used denormalized schema for faster reads and simpler queries. Trade-off: increased storage redundancy.

Snapshot-Based Versioning:
Chosen over in-place updates to ensure auditability and historical tracking.

Rule-Based Conflict Detection:
Used static rules instead of a real drug database. Trade-off: simpler but less clinically comprehensive.

---

## ⚠️ Limitations
- No integration with real clinical drug database
- Simplified rule-based conflict detection
- No authentication or authorization layer

---

## 🔮 Future Enhancements
- Integration with external drug APIs
- Advanced clinical decision support
- Role-based authentication
- Frontend dashboard for visualization

---

## 📸 Screenshots (Recommended)

Add screenshots here:

Swagger API  
MongoDB Collections  

---

## 👨‍💻 Author
Arjun Manohar  
B.Tech Computer Science  
National Institute of Technology Calicut
