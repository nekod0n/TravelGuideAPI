from typing import List, Optional
from sqlalchemy import text, Any
from sqlalchemy.orm import Session
from app.models.place import Place, City, Country
from app.schemas.place import PlaceSearch

def get_places(db: Session, filters: PlaceSearch) -> List[Place]:
    query = db.query(Place)
    if filters.query:
       query = query.filter(Place.name.ilike(f"%{filters.query}%"))
    if filters.category:
        query = query.filter(Place.category == filters.category)
    if filters.city_id:
        query = query.filter(Place.city_id == filters.city_id)
    return query.limit(50).all()

def get_place_by_id(db: Session, place_id: int) -> Optional[Place]:
    result = db.query(Place).join(City).join(Country).filter(Place.place_id == place_id).first()
    return result

def get_nearby_places(db: Session, lat: float, lng: float, radius_km: float = 3.0) -> List[Any]:
    result = db.execute(
        text("SELECT * FROM get_places_nearby(:p_lat, :p_lng, :p_radius_km)"),
        {"p_lat": lat, "p_lng": lng, "p_radius_km": radius_km},
    ).fetchall()