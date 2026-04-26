from pydantic import BaseModel, validator
from datetime import datetime

class ScheduleCreate(BaseModel):
    doctor_id: int
    slot_start: datetime
    slot_end: datetime

    @validator("slot_end")
    def validate_slot(cls, v, values):
        if "slot_start" in values and v <= values["slot_start"]:
            raise ValueError("slot_end must be greater than slot_start")
        return v


class ScheduleResponse(ScheduleCreate):
    id: int

    class Config:
        orm_mode = True