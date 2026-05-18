from fastapi import HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from app.services.review import create_review as create_review_service
from app.database import get_db
from app.schemas.review import ReviewResponse, ReviewCreate
from app.services.review import get_reviews_for_place

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/{place_id}", response_model=List[ReviewResponse])
async def get_reviews_router(place_id: int, db: Session = Depends(get_db)):
    return get_reviews_for_place(db, place_id)

@router.post("/", response_model=ReviewResponse, status_code=201)
async def create_review(user_id: int, data: ReviewCreate, db: Session = Depends(get_db)):
    result = create_review_service(db, user_id, data)
    if not result:
        raise HTTPException(status_code=400, detail="Could not create review")
    return result