from sqlalchemy.orm import Session
from . import models, schemas


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def create_word(db: Session, word: schemas.WordCreate, movie_id: int):
    db_word = models.Word(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

def get_words_by_movie(db: Session, movie_id: int):
    return db.query(models.Word).filter(models.Word.movie_id == movie_id).all()
