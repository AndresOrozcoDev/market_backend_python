from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response
from services.category import CategoryService
from dependencies import validate_api_key


category = APIRouter(
    dependencies=[Depends(validate_api_key)]
)


@category.get('/api/category/all', tags=['Category'], response_model=Response)
async def get_categories():
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content={'message': 'Categories list', 'data':jsonable_encoder(result)})

@category.get('/api/category/{id}', tags=['Category'], response_model=Response)
async def get_category_by_id(id: int):
    db = Session()
    result = CategoryService(db).get_category_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get category success', 'data':jsonable_encoder(result)})

@category.post('/api/category', tags=['Category'], response_model=Response)
async def create_category(name: str = Query()):
    db = Session()
    CategoryService(db).create_category(name)
    return JSONResponse(status_code=200, content={'message': 'category created', 'data':jsonable_encoder(name)})

@category.put('/api/category/{id}', tags=['Category'])
async def update_category(id: int, name: str = Query(), ):
    db = Session()
    result = CategoryService(db).update_category(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category updated'})

@category.delete('/api/category/{id}', tags=['Category'])
async def delete_category(id: int):
    db = Session()
    result = CategoryService(db).delete_category(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category deleted'})

