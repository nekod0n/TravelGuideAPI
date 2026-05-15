from datetime import datetime
from app.database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, Text, Date, DateTime, Boolean, ForeignKey, Float

class Country(Base):
    __tablename__ = "countries"
    country_id = mapped_column(Integer, primary_key=True, index=True)
    country_name = mapped_column(String(100), nullable=False, unique=True)

class City(Base):
    __tablename__ = "cities"
    city_id = mapped_column(Integer, primary_key=True)
    city_name = mapped_column(String(100), nullable=False)
    country_id = mapped_column(Integer, ForeignKey("countries.country_id"))

class Place(Base):
    __tablename__ = "places"
    place_id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255), nullable=False)
    description = mapped_column(Text, nullable=True)
    address = mapped_column(String(500), nullable=True)
    city_id = mapped_column(Integer, ForeignKey("cities.city_id"), nullable=False)
    latitude = mapped_column(Float, nullable=False)
    longitude = mapped_column(Float, nullable=False)
    category = mapped_column(String(50), nullable=False)
    opening_hours = mapped_column(Text, nullable=True)
    average_rating = mapped_column(Float, nullable=True)

class PlacePhoto(Base):
    __tablename__ = "place_photos"
    photo_id = mapped_column(Integer, primary_key=True)
    place_id = mapped_column(Integer, ForeignKey("places.place_id"), nullable=False)
    user_id = mapped_column(Integer, ForeignKey("users.user_id"), nullable=False)
    url = mapped_column(String(500), nullable=False)
    upload_date = mapped_column(DateTime, default=datetime.utcnow)