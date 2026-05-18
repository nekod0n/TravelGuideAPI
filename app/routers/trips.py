from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.trip import TripResponse, TripCreate, TripStopAdd, TripStopResponse
from app.services.trip import create_trip as create_trip_service, get_user_trips, get_trip_by_id, add_stop, delete_trip

router = APIRouter(prefix="/trips", tags=["trips"])

@router.get("/", response_model=List[TripResponse])
async def get_trips(user_id: int, db: Session = Depends(get_db)):
    return get_user_trips(db, user_id)

@router.post("/", response_model=TripResponse, status_code=201)
async def trip_create(user_id: int, data: TripCreate, db: Session = Depends(get_db)):
    return create_trip_service(db, user_id, data)

@router.get("/{trip_id}", response_model=TripResponse)
async def get_trip(trip_id: int, db: Session = Depends(get_db)):
    existing_trip = get_trip_by_id(db, trip_id)
    if existing_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return existing_trip

@router.post("/{trip_id}/stops", response_model=TripStopResponse, status_code=201)
async def add_trip_stop(trip_id: int, data: TripStopAdd, db: Session = Depends(get_db)):
    stop_trip = add_stop(db, trip_id, data)
    if stop_trip is None:
        raise HTTPException(status_code=400, detail="Could not add stop")
    return stop_trip

@router.delete("/{trip_id}", status_code=200)
async def delete_trip_router(trip_id: int, user_id: int, db: Session = Depends(get_db)):
    trip = delete_trip(db, trip_id, user_id)
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip deleted"}
