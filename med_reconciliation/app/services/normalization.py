def normalize_medications(meds):
    normalized = []

    for m in meds:
        normalized.append({
            "name": m.name.strip().lower(),
            "dose": float(m.dose),
            "unit" : m.unit.strip().lower(),
            "status": m.status.strip().lower()
        })
    
    return normalized