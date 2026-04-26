from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.repositories import doctor_repository

def create_doctor(db: Session, data):
    doctor = Doctor(**data.dict())
    return doctor_repository.create_doctor(db, doctor)

def get_all_doctors(db: Session):
    return doctor_repository.get_doctors(db)

def get_doctors_by_department(db: Session, department: str):
    return doctor_repository.get_by_department(db, department)