from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewCreate
from app.services.place import get_place_by_id


def get_reviews_for_place(db: Session ,place_id: int) -> List[Review]:
    result = db.query(Review).filter(Review.place_id == place_id).all()
    return result

def create_review(db: Session, user_id: int, data: ReviewCreate) -> Optional[Review]:
    if not get_place_by_id(db, data.place_id):
        return None
    existing = db.query(Review).filter(Review.user_id == user_id, Review.place_id == data.place_id).first()
    if existing:
        return None
    result = Review(user_id=user_id, place_id=data.place_id, rating=data.rating, comment=data.comment, visit_date=data.visit_date)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

