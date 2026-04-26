from fastapi import FastAPI
from app.api.v1.routes import doctor_routes, schedule_routes

app = FastAPI(title="Doctor Service", version="1.0.0")

app.include_router(doctor_routes.router, prefix="/v1/doctors", tags=["Doctors"])
app.include_router(schedule_routes.router, prefix="/v1/schedules", tags=["Schedules"])

@app.get("/health")
def health_check():
    return {"status": "UP"}