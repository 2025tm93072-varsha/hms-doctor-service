from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name: str
    email: str
    phone: str
    department: str
    specialization: str

class DoctorResponse(DoctorCreate):
    id: int

    class Config:
        orm_mode = True