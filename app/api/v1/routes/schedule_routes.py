from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services import schedule_service
from app.api.v1.schemas.schedule_schema import ScheduleCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_schedule(data: ScheduleCreate, db: Session = Depends(get_db)):
    return schedule_service.create_schedule(db, data)

@router.get("/{doctor_id}")
def get_schedules(doctor_id: int, db: Session = Depends(get_db)):
    return schedule_service.get_schedules(db, doctor_id)