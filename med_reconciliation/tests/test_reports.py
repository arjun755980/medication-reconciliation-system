from app.db import conflicts_col

def test_unresolved_conflicts():

    conflicts_col.insert_many([
        {"patient_id": "p1", "resolved": False},
        {"patient_id": "p1", "resolved": False},
        {"patient_id": "p2", "resolved": True}
    ])

    result = list(conflicts_col.aggregate([
        {"$match": {"resolved": False}},
        {"$group": {"_id": "$patient_id", "count" : {"$sum": 1}}}

    ]))

    assert len(result) == 1
    assert result[0]["_id"] == "p1"