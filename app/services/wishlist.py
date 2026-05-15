from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.wishlist import Wishlist, WishlistItem
from app.schemas.wishlist import WishlistCreate
from app.models.place import Place

def get_user_wishlists(db: Session, user_id: int) -> List[Wishlist]:
    return db.query(Wishlist).filter(Wishlist.user_id == user_id).all()

def create_wishlist(db: Session, user_id: int, data: WishlistCreate) -> Wishlist:
    created_wishlist = Wishlist(user_id = user_id, title = data.title, is_public=data.is_public )
    db.add(created_wishlist)
    db.commit()
    db.refresh(created_wishlist)
    return created_wishlist

def get_wishlist_by_id(db: Session, wishlist_id: int) -> Optional[Wishlist]:
    result = db.query(Wishlist).filter(Wishlist.wishlist_id == wishlist_id).first()
    return result

def add_item_to_wishlist(db: Session, wishlist_id: int, place_id: int, note: Optional[str] = None) -> WishlistItem:
    if not get_wishlist_by_id(db, wishlist_id):
        return None
    is_exist = db.query(Place).filter(Place.place_id == place_id).first()
    if not is_exist:
        return None
    dublicate = db.query(WishlistItem).filter(WishlistItem.wishlist_id == wishlist_id, WishlistItem.place_id == place_id).first()
    if dublicate:
        return None
    add_item = WishlistItem(wishlist_id = wishlist_id, place_id = place_id, note = note)
    db.add(add_item)
    db.commit()
    db.refresh(add_item)
    return add_item