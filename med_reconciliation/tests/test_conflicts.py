import pytest
from app.services.conflict_detection import detect_conflicts


def test_dose_mismatch():
    data = [
        {
            "source_type": "clinic_emr",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"}
            ]
        },
        {
            "source_type": "hospital_discharge",
            "medications": [
                {"name": "aspirin", "dose": 100, "unit": "mg", "status": "active"}
            ]
        }
    ]

    conflicts = detect_conflicts(data)

    assert any(c["type"] == "dose_mismatch" for c in conflicts)


def test_status_conflict():
    data = [
        {
            "source_type": "clinic_emr",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"}
            ]
        },
        {
            "source_type": "patient_reported",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "inactive"}
            ]
        }
    ]

    conflicts = detect_conflicts(data)

    assert any(c["type"] == "status_conflict" for c in conflicts)


def test_no_conflict():
    data = [
        {
            "source_type": "clinic_emr",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"}
            ]
        },
        {
            "source_type": "hospital_discharge",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"}
            ]
        }
    ]

    conflicts = detect_conflicts(data)

    assert len(conflicts) == 0


def test_multiple_conflicts():
    data = [
        {
            "source_type": "clinic_emr",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"},
                {"name": "metformin", "dose": 500, "unit": "mg", "status": "active"}
            ]
        },
        {
            "source_type": "patient_reported",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "inactive"},
                {"name": "metformin", "dose": 850, "unit": "mg", "status": "active"}
            ]
        }
    ]

    conflicts = detect_conflicts(data)

    assert len(conflicts) >= 2


def test_missing_fields():
    data = [
        {
            "source_type": "clinic_emr",
            "medications": [
                {"name": "aspirin", "dose": 75, "unit": "mg", "status": "active"}
            ]
        },
        {
            "source_type": "patient_reported",
            "medications": [
                {"name": "aspirin"}  
            ]
        }
    ]

    try:
        conflicts = detect_conflicts(data)
        assert isinstance(conflicts, list)
    except Exception:
        pytest.fail("Function crashed on missing fields")