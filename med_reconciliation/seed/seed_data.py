from pymongo import MongoClient
from datetime import datetime

client = MongoClient("your_mongodb_connection_string")
db = client.med_db

snapshots_col = db.snapshots
conflicts_col = db.conflicts

def seed_data():
    snapshots_col.delete_many({})
    conflicts_col.delete_many({})

    patients = []

    
    for i in range(1, 11):
        patient_id = f"p{i}"

       
        snapshot1 = {
            "patient_id": patient_id,
            "clinic": "ClinicA" if i <= 5 else "ClinicB",
            "version": 1,
            "timestamp": datetime.utcnow(),
            "sources": [
                {
                    "source_type": "clinic_emr",
                    "medications": [
                        {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"},
                        {"name": "metformin", "dose": 500, "unit": "mg", "status": "active"}
                    ]
                }
            ]
        }

       
        snapshot2 = {
            "patient_id": patient_id,
            "clinic": "ClinicA" if i <= 5 else "ClinicB",
            "version": 2,
            "timestamp": datetime.utcnow(),
            "sources": [
                {
                    "source_type": "patient_reported",
                    "medications": [
                        {"name": "aspirin", "dose": 75, "unit": "mg", "status": "inactive"},  # status conflict
                        {"name": "metformin", "dose": 850, "unit": "mg", "status": "active"}   # dose conflict
                    ]
                }
            ]
        }

        snapshots_col.insert_one(snapshot1)
        snapshots_col.insert_one(snapshot2)

    print(" Seed data inserted")

if __name__ == "__main__":
    seed_data()