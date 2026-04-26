from sqlalchemy.orm import Session
from app.models.doctor import Doctor

def create_doctor(db: Session, doctor):
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_doctors(db: Session):
    return db.query(Doctor).all()

def get_doctor_by_id(db: Session, doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_by_department(db: Session, department: str):
    return db.query(Doctor).filter(Doctor.department == department).all()