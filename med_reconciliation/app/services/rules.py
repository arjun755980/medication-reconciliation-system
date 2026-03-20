
DRUG_CLASSES = { 
    "metformin": "antidiabetic", 
    "insulin": "antidiabetic", 
    "aspirin": "antiplatelet", 
    "clopidogrel": "antiplatelet", 
    "ibuprofen": "nsaid" } 
    
CONFLICTING_CLASSES = { 
    ("antiplatelet", "nsaid"), 
    ("antidiabetic", "antidiabetic") 
    }