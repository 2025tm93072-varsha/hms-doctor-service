from sqlalchemy import Column, Integer, String
from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    department = Column(String)
    specialization = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)