from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from typing import List

class WishlistCreate(BaseModel):
    title: str
    is_public: bool = False

class WishlistResponse(BaseModel):
    model_config = {"from_attributes": True}
    wishlist_id: int
    title: str
    is_public: bool = False
    user_id: int

class WishlistItemAdd(BaseModel):
    place_id: int
    note: Optional[str]

class WishlistItemResponse(BaseModel):
    model_config = {"from_attributes": True}
    item_id: int
    place_id: int
    note: Optional[str]
    added_date: datetime

class WishlistDetailResponse(BaseModel):
    model_config = {"from_attributes": True}
    wishlist_id: int
    title: str
    is_public: bool
    user_id: int
    items: List[WishlistItemResponse] = []