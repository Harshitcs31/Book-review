from pydantic import BaseModel
from typing import Optional

# --------------------
# Book Schemas
# --------------------

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models


# --------------------
# Review Schemas
# --------------------

class ReviewBase(BaseModel):
    reviewer: str
    comment: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True
