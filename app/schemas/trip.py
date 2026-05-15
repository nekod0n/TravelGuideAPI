from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class TripCreate(BaseModel):
    title: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class TripResponse(BaseModel):
    model_config = {"from_attributes": True}
    trip_id: int
    user_id: int
    title: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class TripStopAdd(BaseModel):
    place_id: int
    visit_order: int
    planned_start_time: Optional[datetime] = None
    planned_end_time: Optional[datetime] = None
    transport_type: Optional[str] = None

class TripStopResponse(BaseModel):
    model_config = {"from_attributes": True}
    stop_id: int
    place_id: int
    visit_order: int
    planned_start_time: Optional[datetime] = None
    planned_end_time: Optional[datetime] = None
    transport_type: Optional[str] = None
