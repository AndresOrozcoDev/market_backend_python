from fastapi import APIRouter, Body, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response, Product
from services.supermarket import SupermarketService
from services.category import CategoryService
from services.product import ProductService


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World. Welcome to Market Backen Project with Python and FastAPI!. Please add '/docs' to url"}


@router.get('/api/supermarket/all', tags=['Supermarket'], response_model=Response)
async def get_supermarkets():
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'message': 'Supermarkets list', 'data':jsonable_encoder(result)})

@router.get('/api/supermarket/{id}', tags=['Supermarket'], response_model=Response)
async def get_supermarket_by_id(id: int):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})

@router.post('/api/supermarket', tags=['Supermarket'], response_model=Response)
async def create_supermarket(name: str = Query()):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=200, content={'message': 'Supermarket created', 'data':jsonable_encoder(name)})

@router.put('/api/supermarket/{id}', tags=['Supermarket'])
async def update_supermarket(id: int, name: str = Query()):
    db = Session()
    result = SupermarketService(db).update_supermarket(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked updated'})

@router.delete('/api/supermarket/{id}', tags=['Supermarket'])
async def delete_supermarket(id: int):
    db = Session()
    result = SupermarketService(db).delete_supermarket(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked deleted'})


@router.get('/api/category/all', tags=['Category'], response_model=Response)
async def get_categories():
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content={'message': 'Categories list', 'data':jsonable_encoder(result)})

@router.get('/api/category/{id}', tags=['Category'], response_model=Response)
async def get_category_by_id(id: int):
    db = Session()
    result = CategoryService(db).get_category_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get category success', 'data':jsonable_encoder(result)})

@router.post('/api/category', tags=['Category'], response_model=Response)
async def create_category(name: str = Query()):
    db = Session()
    CategoryService(db).create_category(name)
    return JSONResponse(status_code=200, content={'message': 'category created', 'data':jsonable_encoder(name)})

@router.put('/api/category/{id}', tags=['Category'])
async def update_category(id: int, name: str = Query()):
    db = Session()
    result = CategoryService(db).update_category(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category updated'})

@router.delete('/api/category/{id}', tags=['Category'])
async def delete_category(id: int):
    db = Session()
    result = CategoryService(db).delete_category(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category deleted'})


@router.get('/api/product/all', tags=['Product'], response_model=Response)
async def get_products():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'message': 'Products list', 'data':jsonable_encoder(result)})

@router.get('/api/product/{id}', tags=['Product'], response_model=Response)
async def get_product_by_id(id: int):
    db = Session()
    result = ProductService(db).get_product_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get product success', 'data':jsonable_encoder(result)})

@router.post('/api/product', tags=['Product'], response_model=Response)
async def create_product(product: Product = Body()):
    db = Session()
    result = ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={'message': result})

@router.put('/api/product/{id}', tags=['Product'])
async def update_product(id: int, product: Product = Body()):
    db = Session()
    result = ProductService(db).update_product(id, product)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product updated'})

@router.delete('/api/product/{id}', tags=['Product'])
async def delete_product(id: int):
    db = Session()
    result = ProductService(db).delete_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product deleted'})