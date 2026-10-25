from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import engine
from . import models
from .routers import movies, words
from pathlib import Path

# Создаем таблицы в БД при запуске
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='MovieVocab - Трекер изучения английских слов')

static_dir = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
app.include_router(movies.router, tags=['movies'])
app.include_router(words.router, tags=['words'])

