from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# Главная страница со списком фильмов
@router.get('/', response_class=HTMLResponse)
async def list_movies(request: Request, db: Session = Depends(database.get_db)):
    movies = crud.get_movies(db)
    return templates.TemplateResponse(request,
        'index.html', {
        'request': request,
        'movies': movies
    })

# Создание фильма через форму
@router.post('/movies/create')
async def create_movie(
    title: str = Form(...),
    year: int = Form(None),
    db: Session = Depends(database.get_db)
):
    movie_data = schemas.MovieCreate(title=title, year=year)
    crud.create_movie(db, movie_data)
    return RedirectResponse(url='/', status_code=303)

# Детальная страница со словами
@router.get('/movies/{movie_id}', response_class=HTMLResponse)
async def movie_detail(
    request: Request,
    movie_id: int,
    db: Session = Depends(database.get_db)
):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        return HTMLResponse('Фильм не найден', status_code=404)
    return templates.TemplateResponse(
        request,
        'movie_detail.html', {
            'request': request,
            'movie': movie,
            'words': movie.words
        }
    )