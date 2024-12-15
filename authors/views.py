from fastapi import APIRouter
from authors.schemas import Author

router = APIRouter(prefix='/authors', tags=['authors'])

@router.get('/')
def get_authors():
    return {'authors': '[]'}

@router.get('/{id}')
def get_author_by_id(author: Author):
    return {'author_id': author.id}

@router.put('/{id}')
def update_author(author: Author):
    pass

@router.post('/{id}')
def create_author(author: Author):
    pass

@router.delete('/{id}')
def delete_author(author: Author):
    pass
