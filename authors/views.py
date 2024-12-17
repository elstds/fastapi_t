from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from authors.schemas import Author, AuthorCreate
from . import crud
from core.models import db_h

router = APIRouter(prefix='/authors', tags=['authors'])

@router.get('/', response_model=list[Author])
async def get_authors(
    session: AsyncSession = Depends(db_h.scope_session_dependency),
):
    return await crud.get_authors(session=session)


@router.post('/', response_model=Author)
async def create_author(
    author_in: AuthorCreate,
    session: AsyncSession = Depends(db_h.scope_session_dependency)
):
    return await crud.create_author(session=session, author_in=author_in)


@router.get('/{id}', response_model=Author)
async def get_author_by_id(
    author_id: int,
    session: AsyncSession = Depends(db_h.scope_session_dependency)
):
    author = await crud.get_author_by_id(session=session, author_id=author_id)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Author with id {author_id} not found'
    )


# @router.put('/{id}')
# async def update_author(author: Author):
#     pass


# @router.delete('/{id}')
# async def delete_author(author: Author):
#     pass
