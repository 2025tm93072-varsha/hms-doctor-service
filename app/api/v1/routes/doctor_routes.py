from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.doctor import Doctor
from app.services import doctor_service
import os

router = APIRouter()

# ✅ DEFINE THIS FIRST
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ ROUTES AFTER

@router.get("/")
def get_doctors():
    print("WORKING DIR:", os.getcwd())
    
    db = SessionLocal()
    try:
        doctors = db.query(Doctor).all()
        print("DOCTOR COUNT FROM API:", len(doctors))
        return doctors
    finally:
        db.close()

@router.post("/book/{doctor_id}")
def book_doctor(doctor_id: int, db: Session = Depends(get_db)):
    return doctor_service.book_and_pay(db, doctor_id)