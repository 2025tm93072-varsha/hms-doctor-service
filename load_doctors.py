import csv
from datetime import datetime
from app.db.session import SessionLocal
from app.models.doctor import Doctor

db = SessionLocal()

inserted_count = 0
skipped_count = 0

with open("hms_doctors_indian.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("ADDING:", row["name"])
        # Check if doctor already exists (by email)
        existing = db.query(Doctor).filter(Doctor.email == row["email"]).first()

        if existing:
            skipped_count += 1
            continue

        doctor = Doctor(
            name=row["name"],
            email=row["email"],
            phone=row["phone"],
            department=row["department"],
            specialization=row["specialization"],
            created_at=datetime.fromisoformat(row["created_at"])
        )

        db.add(doctor)
        inserted_count += 1

# Commit changes
db.commit()

# Debug output
print(f"Inserted: {inserted_count}")
print(f"Skipped (duplicates): {skipped_count}")

# Optional: total count in DB
total = db.query(Doctor).count()
print(f"Total doctors in DB: {total}")

db.close()

print("Doctors loaded successfully!")