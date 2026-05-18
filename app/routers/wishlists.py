from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.wishlist import WishlistResponse, WishlistCreate, WishlistItemAdd, WishlistItemResponse
from app.services.wishlist import get_user_wishlists, create_wishlist, get_wishlist_by_id, add_item_to_wishlist as add_item_service
from app.schemas.wishlist import WishlistResponse, WishlistCreate, WishlistItemAdd, WishlistItemResponse, WishlistDetailResponse

router = APIRouter(prefix="/wishlists", tags=["wishlists"])

@router.get("/", response_model=List[WishlistResponse])
async def get_wishlists(user_id: int, db: Session = Depends(get_db)):
    return get_user_wishlists(db, user_id)

@router.post("/", response_model=WishlistResponse, status_code=201)
async def create_user_wishlist(user_id: int, data: WishlistCreate, db: Session = Depends(get_db)):
    return create_wishlist(db, user_id, data)

@router.get("/{wishlist_id}", response_model=WishlistDetailResponse)
async def get_wishlist_by_id_router(wishlist_id: int, db: Session = Depends(get_db)):
    wishlist = get_wishlist_by_id(db, wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wishlist

@router.post("/{wishlist_id}/items", response_model=WishlistItemResponse, status_code=201)
async def add_item_to_wishlist_router(wishlist_id: int, data: WishlistItemAdd, db: Session = Depends(get_db)):
    add_to_wishlist = add_item_service(db, wishlist_id, data.place_id, data.note)
    if not add_to_wishlist:
        raise HTTPException(status_code=400, detail="Could not add item")
    return add_to_wishlist

@router.delete("/{wishlist_id}")
async def delete_wishlist_router(wishlist_id: int, user_id: int, db: Session = Depends(get_db)):
    wishlist = get_wishlist_by_id(db, wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    if wishlist.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    db.delete(wishlist)
    db.commit()
    return {"message": "Wishlist deleted"}