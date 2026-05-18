from typing import List, Optional
from sqlalchemy.orm import Session

from app.models import trip
from app.models.trip import Trip, TripStop
from app.schemas.trip import TripCreate, TripStopAdd


def get_user_trips(db: Session, user_id: int) -> List[Trip]:
    return db.query(Trip).filter(Trip.user_id==user_id).all()

def create_trip(db: Session, user_id: int, data: TripCreate) -> Trip:
    trip = Trip(user_id=user_id, title=data.title, start_date=data.start_date, end_date=data.end_date)
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

def get_trip_by_id(db: Session, trip_id: int) -> Optional[Trip]:
    return db.query(Trip).filter(Trip.trip_id == trip_id).first()

def add_stop(db: Session, trip_id: int, data: TripStopAdd) -> Optional[TripStop]:
    if not get_trip_by_id(db, trip_id):
        return None
    tripStop = TripStop(trip_id=trip_id, place_id=data.place_id, visit_order=data.visit_order, planned_start_time=data.planned_start_time, planned_end_time=data.planned_end_time, transport_type=data.transport_type)
    db.add(tripStop)
    db.commit()
    db.refresh(tripStop)
    return tripStop

def delete_trip(db: Session, trip_id: int, user_id: int) -> Optional[Trip]:
    trip = get_trip_by_id(db, trip_id)
    if not trip:
        return None
    if trip.user_id != user_id:
        return None
    db.delete(trip)
    db.commit()
    return trip

