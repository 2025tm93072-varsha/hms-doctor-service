from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.repositories import doctor_repository
from app.services.external_services import call_payment_service, call_notification_service

def create_doctor(db: Session, data):
    doctor = Doctor(**data.dict())
    return doctor_repository.create_doctor(db, doctor)

def get_all_doctors(db: Session):
    return doctor_repository.get_doctors(db)

def get_doctors_by_department(db: Session, department: str):
    return doctor_repository.get_by_department(db, department)

def book_and_pay(db, doctor_id):
    # 1. Get doctor
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        return {"error": "Doctor not found"}

    # 2. Call payment service
    payment = call_payment_service(patient_id=doctor_id, amount=500)

    # 3. Call notification service
    message = f"Appointment confirmed with Dr. {doctor.name}"
    notification = call_notification_service(doctor.email, message)

    return {
        "doctor": doctor.name,
        "payment": payment,
        "notification": notification
    }