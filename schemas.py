# schemas.py
from pydantic import BaseModel, Field
from typing import Optional
import datetime


class ClinicalDataCreate(BaseModel):
    patient_name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, le=120, example=45)
    diagnosis: str = Field(..., example="Hypertension")
    blood_pressure: str = Field(..., example="120/80")
    heart_rate: int = Field(..., ge=0, le=250, example=72)
    medications: str = Field(..., example="Lisinopril")


# The read schema includes the auto generated fields
class ClinicalDataRead(ClinicalDataCreate):
    id: int
    recorded_at: datetime.datetime
    blood_pressure: Optional[str] = None
    heart_rate: Optional[int] = None
    medications: Optional[str] = None
