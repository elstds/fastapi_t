from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from authors.schemas import Author, AuthorCreate, AuthorBase
from . import crud
from core.models import db_h
from .dependencies import author_by_id

router = APIRouter(prefix='/authors', tags=['authors'])

@router.get('/', response_model=list[Author])
async def get_authors(
    session: AsyncSession = Depends(db_h.scope_session_dependency),
):
    return await crud.get_authors(session=session)


@router.post('/', response_model=Author, status_code=status.HTTP_201_CREATED)
async def create_author(
    author_in: AuthorCreate,
    session: AsyncSession = Depends(db_h.scope_session_dependency)
):
    return await crud.create_author(session=session, author_in=author_in)


@router.get('/{id}', response_model=Author)
async def get_author(
    author: Author = Depends(author_by_id)
):
    return author


@router.put('/{id}')
async def update_author(
        author_in: AuthorBase,
        author: Author = Depends(author_by_id),
        session: AsyncSession = Depends(db_h.scope_session_dependency)
) -> Author:
    return await crud.update_author(
        session=session,
        upd_author=author_in,
        author=author
    )


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(
    author: Author = Depends(author_by_id),
    session: AsyncSession = Depends(db_h.scope_session_dependency)
) -> None:
    await crud.delete_author(session=session, author=author)
