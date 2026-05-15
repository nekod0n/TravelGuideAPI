from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PlaceResponse(BaseModel):
    model_config = {"from_attributes": True}
    place_id: int
    name: str
    description: Optional[str] = None
    address: Optional[str] = None
    city_name: Optional[str] = None
    country_name: Optional[str] = None
    latitude: float
    longitude: float
    category: str
    opening_hours: Optional[str] = None
    average_rating: Optional[float] = None

class PlaceSearch(BaseModel):
    query: Optional[str] = None
    category: Optional[str] = None
    city_id: Optional[int] = None

class PlaceNearby(BaseModel):
    latitude: float
    longitude: float
    radius_km: float = 3.0

class PlacePhotoResponse(BaseModel):
    model_config = {"from_attributes": True}
    photo_id: int
    url: str
    upload_date: datetime


