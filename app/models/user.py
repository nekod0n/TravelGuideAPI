from datetime import datetime
from app.database import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, Text, Date, DateTime, Boolean

class User(Base):
    __tablename__ = 'users'
    user_id = mapped_column(Integer, primary_key=True, index=True)
    email = mapped_column(String(255), unique=True, nullable=False)
    password_hash = mapped_column(Text, nullable=False)
    first_name = mapped_column(String(100), nullable=False)
    last_name = mapped_column(String(100), nullable=True)
    date_of_birth = mapped_column(Date, nullable=True)
    registration_date = mapped_column(DateTime, default=datetime.utcnow)
    preferred_language = mapped_column(String(10), default='ru')
    is_active = mapped_column(Boolean, default=True)

