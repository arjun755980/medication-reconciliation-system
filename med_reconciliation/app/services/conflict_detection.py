from app.services.rules import DRUG_CLASSES, CONFLICTING_CLASSES

def detect_conflicts(all_sources):
    conflicts = []
    med_map = {}
    seen = set()
  
    for src in all_sources:
        for med in src["medications"]:
            name = med["name"]

            if name not in med_map:
                med_map[name] = []

            med_map[name].append({
                "source": src.get("source_type"),
                "dose": med.get("dose"),
                "unit": med.get("unit"),
                "status": med.get("status")
            })
  
   
    for name, entries in med_map.items():

        doses = set(e["dose"] for e in entries)
        statuses = set(e["status"] for e in entries)

        key = ("dose_mismatch", name)
        if len(doses) > 1 and key not in seen:
            seen.add(key)
            conflicts.append({
                "type": "dose_mismatch",
                "medication": name,
                "details": entries,
                "resolved": False
            })

        key = ("status_conflict", name)
        if "active" in statuses and "inactive" in statuses and key not in seen:
            seen.add(key)
            conflicts.append({
                "type": "status_conflict",
                "medication": name,
                "details": entries,
                "resolved": False
            })


    meds = list(med_map.keys())

    for i in range(len(meds)):
        for j in range(i+1, len(meds)):
            m1, m2 = meds[i], meds[j]

            c1 = DRUG_CLASSES.get(m1)
            c2 = DRUG_CLASSES.get(m2)

            key = ("interaction", m1, m2)

            if c1 and c2  :
                if (c1, c2) in CONFLICTING_CLASSES or (c2, c1) in CONFLICTING_CLASSES:
                    if key not in seen:
                        seen.add(key)
                        conflicts.append({
                        "type" : "drug_interaction",
                        "medications" : [m1, m2],
                        "resolved": False
                        })
    

    return conflicts