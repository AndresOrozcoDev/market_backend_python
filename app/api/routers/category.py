from fastapi import APIRouter, Query, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.db.database import Session
from app.api.interfaces.interfaces import Response
from app.services.category import CategoryService
from dependencies import validate_api_key


category = APIRouter(
    prefix="/api/category",
    tags=["Category"],
    dependencies=[Depends(validate_api_key)]
)


@category.get('/all', response_model=Response)
async def get_categories():
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Categories list', 'data':jsonable_encoder(result)})

@category.get('/{id}', response_model=Response)
async def get_category_by_id(id: int):
    db = Session()
    result = CategoryService(db).get_category_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Get category success', 'data':jsonable_encoder(result)})

@category.post('', response_model=Response)
async def create_category(name: str = Body()):
    db = Session()
    CategoryService(db).create_category(name)
    return JSONResponse(status_code=201, content={'status_code': 201, 'message': 'Category created', 'data':jsonable_encoder(name)})

@category.put('/{id}')
async def update_category(id: int, name: str = Body(), ):
    db = Session()
    result = CategoryService(db).update_category(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Category updated'})

@category.delete('/{id}')
async def delete_category(id: int):
    db = Session()
    result = CategoryService(db).delete_category(id)
    if not result:
        return JSONResponse(status_code=404, content={'status_code': 404, 'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'status_code': 200, 'message': 'Category deleted'})

