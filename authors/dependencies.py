from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_h, Author

from . import crud


async def author_by_id(
        author_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_h.scope_session_dependency)
) -> Author:
    author = await crud.get_author_by_id(session, author_id)
    if author:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found",
    )