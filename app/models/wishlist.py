from datetime import datetime
from sqlalchemy import Integer, ForeignKey, Boolean, Text, String, DateTime
from sqlalchemy.orm import mapped_column
from app.database import Base


class Wishlist(Base):
    __tablename__ = 'wishlists'
    wishlist_id = mapped_column(Integer, primary_key=True, index=True)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = mapped_column(String(255), nullable=False)
    is_public = mapped_column(Boolean, default=False)

class WishlistItem(Base):
    __tablename__ = 'wishlist_items'
    item_id = mapped_column(Integer, primary_key=True, index=True)
    wishlist_id = mapped_column(Integer, ForeignKey('wishlists.wishlist_id'), nullable=False)
    place_id = mapped_column(Integer, ForeignKey('places.place_id'), nullable=False)
    note = mapped_column(Text, nullable=True)
    added_date = mapped_column(DateTime, nullable=False, default=datetime.utcnow)