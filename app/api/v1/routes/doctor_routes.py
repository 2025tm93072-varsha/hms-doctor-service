from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.doctor import Doctor
import os

router = APIRouter()

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