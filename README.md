# Medication Reconciliation & Conflict Reporting Service

## Overview

This project is a FastAPI-based backend system that ingests medication data from multiple sources, detects conflicts across those sources, and provides reporting for unresolved conflicts.

It simulates a real-world healthcare scenario where patient medication data may originate from different systems (such as clinics, hospitals, or patient input) and may contain inconsistencies.

---

## Key Features

- Multi-source medication ingestion  
- Versioned snapshots (history preserved)  
- Conflict detection:
  - Dose mismatch  
  - Status conflict (active vs inactive)  
  - Drug interaction (rule-based)  
- Conflict resolution with audit trail  
- Reporting and aggregation endpoints  
- MongoDB-based storage  

---

## Tech Stack

- Backend: FastAPI (Python 3.12)  
- Database: MongoDB  
- Driver: PyMongo  
- API Testing: Swagger UI (/docs)  

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/arjun755980/medication-reconciliation-system.git  
cd medication-reconciliation-system  

---

### 2. Create virtual environment

python3 -m venv venv  
source venv/bin/activate  

---

### 3. Install dependencies

pip install -r requirements.txt  

---

### 4. Setup MongoDB

#### Option A: Local MongoDB
Ensure MongoDB is installed and running on your system.

#### Option B: MongoDB Atlas
- Create a free cluster  
- Create a database user  
- Allow network access  
- Copy the connection string  
- Update it in your db.py  

---

### 5. Run the server

uvicorn app.main:app --reload  

---

### 6. Open Swagger UI

http://127.0.0.1:8000/docs  

---

## Seeding Test Data

A seed script is included to populate the database with sample data.

Run:

python seed/seed_data.py  

This will:
- Insert sample patient snapshots  
- Generate conflicts (dose mismatch, status conflict, drug interactions)  
- Help test reporting endpoints easily  

---

## API Endpoints

### Ingestion

POST /patients/{patient_id}/medications  

### Reports

GET /report/clinic/{clinic_name}  
GET /report/conflicts/summary  

### Conflict Resolution

POST /conflicts/{conflict_id}/resolve  

---

## MongoDB Schema

### Snapshots Collection

Stores versioned medication data.

Fields:
- patient_id  
- version  
- timestamp  
- sources  
  - source_type  
  - medications  
    - name  
    - dose  
    - unit  
    - status  

---

### Conflicts Collection

Stores detected conflicts.

Fields:
- patient_id  
- type (dose_mismatch, status_conflict, drug_interaction)  
- medication / medications  
- details  
- resolved  
- timestamp  
- resolution (reason, resolved_at)  

---

## Sample Conflict Document

{<br>
  "patient_id": "p1", <br>
  "type": "dose_mismatch",<br>
  "medication": "aspirin",<br>
  "details": [<br>
    {<br>
      "source": "clinic_emr",<br>
      "dose": 75,<br>
      "unit": "mg",<br>
      "status": "active"<br>
    },<br>
    {<br>
      "source": "hospital_discharge",<br>
      "dose": 100,<br>
      "unit": "mg",<br>
      "status": "active"<br>
    }<br>
  ],<br>
  "resolved": false,<br>
  "timestamp": "2026-03-20T10:00:00Z"<br>
}<br>

---

## Conflict Detection Logic

### 1. Dose Mismatch
Same medication appears with different doses across sources.

### 2. Status Conflict
Medication marked active in one source and inactive in another.

### 3. Drug Interaction
Two medications belong to conflicting drug classes based on predefined rules.

---

## Conflict Rules

Drug interaction rules are defined in the project (rules file).

Example conflicting combinations:
- aspirin + warfarin  
- ibuprofen + warfarin  

These simulate real-world unsafe drug combinations.

---

## Indexing Strategy

- patient_id → quick lookup  
- resolved → filter unresolved conflicts  
- timestamp → time-based queries  

---

## Testing

Run tests using:

PYTHONPATH=. pytest  

Covers:
- Conflict detection edge cases  
- Aggregation logic  

---

## Design Decisions

### Versioning
Each ingestion creates a new snapshot instead of overwriting data.  
This preserves history and ensures auditability.

### Conflict Detection on Write
Conflicts are detected during ingestion, making reporting faster.

### Denormalization
Patient-related data is stored with conflicts to simplify queries.

---

## Author

Arjun Manohar  
B.Tech Computer Science  
NIT Calicut  

GitHub: https://github.com/arjun755980  

---

## Notes

- This project uses static rules instead of a real drug database  
- Designed for academic and demonstration purposes  
