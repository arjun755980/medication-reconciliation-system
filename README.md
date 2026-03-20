# 🏥 Medication Reconciliation System

## 📌 Overview
This project is a **FastAPI-based backend system** for managing patient medication data from multiple sources and detecting conflicts.

It supports:
- Multi-source medication ingestion
- Conflict detection across sources
- Versioned medication snapshots
- Conflict resolution tracking
- Aggregation and reporting

---

## 🚀 Features

### 🔹 Ingestion
- Accept medication data from different sources:
  - `clinic_emr`
  - `hospital_discharge`
  - `patient_reported`

### 🔹 Normalization
- Converts medication names to lowercase
- Ensures consistent units and structure

### 🔹 Conflict Detection
Detects:
- ✅ Dose mismatch (same drug, different dose)
- ✅ Status conflict (active vs inactive)
- ✅ Drug interaction (based on predefined rules)

### 🔹 Versioning
- Each ingestion creates a new **snapshot version**
- Maintains longitudinal medication history

### 🔹 Conflict Resolution
- Mark conflicts as resolved
- Store resolution reason and timestamp

### 🔹 Reporting
- Patients with unresolved conflicts per clinic
- Patients with ≥ 2 conflicts in last 30 days

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **Database:** MongoDB Atlas  
- **Driver:** PyMongo  
- **Testing:** Pytest  

---

## 📂 Project Structure
