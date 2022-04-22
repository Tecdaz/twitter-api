# Python
from datetime import date
from typing import Optional
from uuid import UUID

# FastAPI
from fastapi import FastAPI
# Pydantic
from pydantic import Field, EmailStr, BaseModel

app = FastAPI()


# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8
    )


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


@app.get(path="/")
def home():
    return {"Twitter API": "Hello world"}
