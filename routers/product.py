from fastapi import APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response, Product
from services.product import ProductService
from dependencies import validate_api_key


product = APIRouter(
    dependencies=[Depends(validate_api_key)]
)


@product.get('/api/product/all', tags=['Product'], response_model=Response)
async def get_products():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'message': 'Products list', 'data':jsonable_encoder(result)})

@product.get('/api/product/{id}', tags=['Product'], response_model=Response)
async def get_product_by_id(id: int):
    db = Session()
    result = ProductService(db).get_product_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get product success', 'data':jsonable_encoder(result)})

@product.post('/api/product', tags=['Product'], response_model=Response)
async def create_product(product: Product = Body()):
    db = Session()
    result = ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={'message': result})

@product.put('/api/product/{id}', tags=['Product'])
async def update_product(id: int, product: Product = Body()):
    db = Session()
    result = ProductService(db).update_product(id, product)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product updated'})

@product.delete('/api/product/{id}', tags=['Product'])
async def delete_product(id: int):
    db = Session()
    result = ProductService(db).delete_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product deleted'})

