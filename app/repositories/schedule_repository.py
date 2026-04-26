from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from sqlalchemy import and_

def create_schedule(db: Session, schedule):
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule

def get_schedules_by_doctor(db: Session, doctor_id: int):
    return db.query(Schedule).filter(Schedule.doctor_id == doctor_id).all()


def check_slot_conflict(db: Session, doctor_id: int, start, end):
    return db.query(Schedule).filter(
        Schedule.doctor_id == doctor_id,
        and_(
            Schedule.slot_start < end,
            Schedule.slot_end > start
        )
    ).first()