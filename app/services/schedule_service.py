from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.schedule import Schedule
from app.repositories import schedule_repository

def create_schedule(db: Session, data):
    
    # 🔥 Conflict Check
    conflict = schedule_repository.check_slot_conflict(
        db,
        data.doctor_id,
        data.slot_start,
        data.slot_end
    )

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Slot conflict: Doctor already has a booking in this time range"
        )

    schedule = Schedule(**data.dict())
    return schedule_repository.create_schedule(db, schedule)


def get_schedules(db: Session, doctor_id: int):
    return schedule_repository.get_schedules_by_doctor(db, doctor_id)