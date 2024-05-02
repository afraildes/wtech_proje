from pydantic import BaseModel

class Patients(BaseModel):
    
    age:int
    anaemia:int
    creatinine_phosphokinase:int
    diabetes:int
    ejection_fraction:int
    high_blood_pressure:int
    platelets:float
    serum_creatinine:float
    serum_sodium:float
    smoking:int
    time:int

    