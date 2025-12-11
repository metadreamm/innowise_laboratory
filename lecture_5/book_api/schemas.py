from pydantic import BaseModel, Field
from typing import Optional

# Base schema for data coming IN (to create or update a book)
class BookBase(BaseModel):
    # Field(...) can be used to add metadata like min/max values
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: Optional[int] = None

# Schema used for creating a new book (inherits all fields from BookBase)
class BookCreate(BookBase):
    pass

# Schema used for displaying a book
class Book(BookBase):
    id: int

    # Configuration class for SQLAlchemy ORM compatibility
    class Config:
        orm_mode = True