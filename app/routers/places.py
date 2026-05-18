from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.place import PlaceResponse, PlaceSearch, PlaceNearby, PlacePhotoResponse
from app.services.place import get_nearby_places as get_nearby_places_service, get_place_by_id, get_places
from app.models.place import PlacePhoto
import os

router = APIRouter(prefix="/places", tags=["places"])

@router.get("/", response_model=List[PlaceResponse])
async def get_all_places(filters: PlaceSearch = Depends(), db: Session = Depends(get_db)):
    return get_places(db, filters)

@router.get("/nearby", response_model=List[PlaceResponse])
async def get_nearby_places(filters: PlaceNearby = Depends(), db: Session = Depends(get_db)):
    result = get_nearby_places_service(db, filters.latitude, filters.longitude, filters.radius_km)
    if not result:
        return []
    return result

@router.get("/{place_id}", response_model=PlaceResponse)
async def get_place(place_id: int, db: Session = Depends(get_db)):
    place = get_place_by_id(db, place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place

@router.post("/{place_id}/photos", response_model=PlacePhotoResponse, status_code=201)
async def upload_photo(
    place_id: int,
    file: UploadFile = File(...),
    user_id: int = None,
    db: Session = Depends(get_db),
):
    place = get_place_by_id(db, place_id)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")

    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{place_id}_{file.filename}"
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    photo = PlacePhoto(
        place_id=place_id,
        user_id=user_id or 1,
        url=file_path,
    )
    db.add(photo)
    db.commit()
    db.refresh(photo)
    return photo

@router.get("/{place_id}/photos", response_model=List[PlacePhotoResponse])
async def get_photos(place_id: int, db: Session = Depends(get_db)):
    return db.query(PlacePhoto).filter(PlacePhoto.place_id == place_id).all()