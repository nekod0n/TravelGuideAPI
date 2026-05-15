from datetime import datetime, date
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    place_id: int
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    visit_date: Optional[date] = None

class ReviewResponse(BaseModel):
    model_config = {"from_attributes": True}
    review_id: int
    user_id: int
    place_id: int
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    visit_date: Optional[date] = None
    created_at: datetime