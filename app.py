from fastapi import FastAPI
from core.models import Base, db_h
from authors.views import router as authors_r
from books.views import router as books_r
from borrows.views import router as borrows_r
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_h.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(lifespan=lifespan)
app.include_router(authors_r)
app.include_router(books_r)
app.include_router(borrows_r)
