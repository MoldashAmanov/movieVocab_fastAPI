from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class WordBase(BaseModel):
    english: str
    russian: str
    context: Optional[str] = None


class WordCreate(WordBase):
    pass


class Word(WordBase):
    id: int
    movie_id: int
    created_at: datetime
    class Config:
        from_attributes = True


class MovieBase(BaseModel):
    title: str
    year: Optional[int] = None
    description: Optional[str] = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int
    created_at: datetime
    words: List[Word]
    class Config:
        from_attributes = True
        