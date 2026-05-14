from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=25)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: Optional[str] = Field(default= None, min_length=1, max_length=100)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=25)

class UserResponse(BaseModel):
    model_config = {"from_attributes": True}
    user_id: int
    email: EmailStr
    first_name: str
    last_name: Optional[str]
    registration_date: datetime

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"