
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Author
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import AuthorCreate

async def get_authors(session: AsyncSession) -> list[Author]:
    querry = select(Author).order_by(Author.id)
    result: Result = await session.execute(querry)
    authors = result.scalars().all()
    return list(authors)

async def get_author_by_id(session: AsyncSession, author_id: int) -> Author | None:
    querry = select(Author).where(Author.id == author_id)
    result: Result = await session.execute(querry)
    author = result.scalar()
    return author

async def create_author(session: AsyncSession, author_in: AuthorCreate) -> Author:
    author = Author(**author_in.model_dump())
    session.add(author)
    await session.commit()
    await session.refresh(author)
    return author
