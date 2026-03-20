from fastapi import APIRouter
from app.db import conflicts_col
from datetime import datetime, timedelta
from bson import ObjectId

router = APIRouter()

@router.get("/report/clinic/{clinic_name}")
def patients_with_conflicts(clinic_name: str):

    patients = conflicts_col.distinct("patient_id", {"resolved": False, "clinic" : clinic_name})
    return {
        "clinic" : clinic_name,
        "patients": patients
        }
    
@router.get("/report/conflicts/summary")
def conflict_summary():

    last_30_days = datetime.utcnow() - timedelta(days = 30)

    pipeline = [
        {
            "$match": {
                "resolved" : False,
                "created_at": {"$gte" : last_30_days}
            }
        },
        {
            "$group": {
                "_id": "$patient_id",
                "count": {"$sum" : 1}
            }
        },
        {
            "$match":{
                "count": {"$gte":2}
            }
        }
    ]

    result = list(conflicts_col.aggregate(pipeline))

    return {
        "patients_with_2plus_conflicts" : len(result),
        "patients" : result
    }

@router.post("/conflicts/{conflict_id}/resolve")
def resolve_conflict(conflict_id: str, reason: str ):

    result = conflicts_col.update_one(
        {"_id": ObjectId(conflict_id)},
        {
            "$set": {
                "resolved": True,
                "resolution": {
                    "reason": reason,
                    "resolved_at": datetime.utcnow()
                }
            }
        }
    )
    print("Matched:" , result.matched_count)
    print("Modified:", result.modified_count)
    return {"message": "conflict resolved"}

