from sqlalchemy import Integer, ForeignKey, String, Date, DateTime
from sqlalchemy.orm import mapped_column
from app.database import Base


class Trip(Base):
    __tablename__ = 'trips'
    trip_id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = mapped_column(String(255), nullable=False)
    start_date = mapped_column(Date, nullable=True)
    end_date = mapped_column(Date, nullable=True)

class TripStop(Base):
    __tablename__ = 'trip_stops'
    stop_id = mapped_column(Integer, primary_key=True)
    trip_id = mapped_column(Integer, ForeignKey('trips.trip_id'), nullable=False)
    place_id = mapped_column(Integer, ForeignKey('places.place_id'), nullable=False)
    visit_order = mapped_column(Integer, nullable=False)
    planned_start_time = mapped_column(DateTime, nullable=True)
    planned_end_time = mapped_column(DateTime, nullable=True)
    transport_type = mapped_column(String(20), nullable=True)