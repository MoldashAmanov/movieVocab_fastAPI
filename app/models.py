from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связь: у одного фильма много слов
    words = relationship('Word', back_populates='movie', cascade='all, delete-orphan')


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, index=True)
    russian = Column(String)
    context = Column(Text, nullable=True) # Предложение из фильма
    movie_id = Column(Integer, ForeignKey('movies.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    movie = relationship('Movie', back_populates='words')