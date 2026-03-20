from fastapi import APIRouter
from app.schemas import ingestionRequest
from app.db import snapshots_col, conflicts_col 
from app.services.normalization import normalize_medications
from app.services.conflict_detection import detect_conflicts
from datetime import datetime

router = APIRouter()

@router.post("/patients/{patient_id}/medications")
def ingest(patient_id: str, data: ingestionRequest):

    meds = normalize_medications(data.medications)

    last_snapshot = snapshots_col.find_one(
        {"patient_id": patient_id},
        sort = [("version", -1)]
    )

    version = 1 if not last_snapshot else last_snapshot["version"]+1

    snapshot = {
        "patient_id": patient_id,
        "clinic": data.clinic,
        "version": version,
        "created_at": datetime.utcnow(),
        "sources": [
            {
            "source_type": data.source,
            "medications": meds
            }
        ]
    }

    snapshots_col.insert_one(snapshot)
    all_snapshots = list(snapshots_col.find({"patient_id" : patient_id}))
    #conflicts = detect_conflicts(snapshot["sources"])

    all_sources = []
    for snap in all_snapshots:
        all_sources.extend(snap["sources"])

    conflicts = detect_conflicts(all_sources)

    conflicts_col.delete_many({"patient_id": patient_id})

    for c in conflicts:
        c["patient_id"] = patient_id
        c["clinic"] = data.clinic
        c["created_at"] = datetime.utcnow()
        c["resolved"] = False
        c["resolution"] = None
        conflicts_col.insert_one(c)
    
    return {"message" : "ingested", "conflicts": len(conflicts)}