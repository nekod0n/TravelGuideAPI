from datetime import datetime
from sqlalchemy import Integer, ForeignKey, Text, Date, DateTime
from sqlalchemy.orm import mapped_column
from app.database import Base


class Review(Base):
    __tablename__ = 'reviews'
    review_id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey('users.user_id'), nullable=False)
    place_id = mapped_column(Integer, ForeignKey('places.place_id'), nullable=False)
    rating = mapped_column(Integer, nullable=False)
    comment = mapped_column(Text, nullable=True)
    visit_date = mapped_column(Date, nullable=True)
    created_at = mapped_column(DateTime, default=datetime.utcnow)
