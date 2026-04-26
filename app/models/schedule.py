from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.session import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    slot_start = Column(DateTime)
    slot_end = Column(DateTime)