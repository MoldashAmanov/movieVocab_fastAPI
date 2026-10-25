from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()
templates = Jinja2Templates(directory='templates')

# Страница добавления слова к конкретному фильму
@router.get('/movies/{movie_id}/add-word', response_class=HTMLResponse)
async def add_word_page(
    request: Request,
    movie_id: int,
    db: Session = Depends(database.get_db)
):
    movie = crud.get_movie(db, movie_id)
    return templates.TemplateResponse(
        request,
        'add_word.html', {
            "request": request,
            'movie': movie
        }
    )

#  Обработка добавления слова
@router.post('/movies/{movie_id}/add-word')
async def create_word(
    movie_id: int,
    english: str = Form(...),
    russian: str = Form(...),
    context: str = Form(None),
    db: Session = Depends(database.get_db)
):
    word_data = schemas.WordCreate(
        english=english, russian=russian, context=context
    )
    crud.create_word(db, word_data, movie_id)
    return RedirectResponse(url=f"/movies/{movie_id}", status_code=303)
