from pydantic import BaseModel
from typing import List

class Medication(BaseModel):
    name : str
    dose : float
    unit : str
    status : str

class ingestionRequest(BaseModel):
    source : str
    clinic: str
    medications: List[Medication]