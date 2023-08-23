from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
    author: str
    title: str
    year: Optional[int] = None

class BookCreate(BookBase):
    pass

class BookInDB(BookBase):
    id: int

