import os

from dotenv import load_dotenv
from fastapi import APIRouter, Body, Query, HTTPException, Depends, Header
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from utils.interfaces import Response, Product, User
from services.supermarket import SupermarketService
from services.category import CategoryService
from services.product import ProductService
from services.user import UserService


router = APIRouter()


async def validate_api_key(api_key: str = Header()):
    load_dotenv()
    if api_key != os.getenv('API-KEY'):
        raise HTTPException(status_code = 401, detail = "API Key inválida")
    


@router.get("/")
async def root(api_key: str = Depends(validate_api_key)):
    return {"message": "Welcome to Market Backend Project with Python and FastAPI!. Please add '/docs' to url"}



@router.get('/api/supermarket/all', tags=['Supermarket'], response_model=Response)
async def get_supermarkets(api_key: str = Depends(validate_api_key)):
    db = Session()
    result = SupermarketService(db).get_supermarkets()
    return JSONResponse(status_code=200, content={'message': 'Supermarkets list', 'data':jsonable_encoder(result)})

@router.get('/api/supermarket/{id}', tags=['Supermarket'], response_model=Response)
async def get_supermarket_by_id(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = SupermarketService(db).get_supermarket_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found Supermarket', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get Supermarket success', 'data':jsonable_encoder(result)})

@router.post('/api/supermarket', tags=['Supermarket'], response_model=Response)
async def create_supermarket(name: str = Query(), api_key: str = Depends(validate_api_key)):
    db = Session()
    SupermarketService(db).create_supermarket(name)
    return JSONResponse(status_code=200, content={'message': 'Supermarket created', 'data':jsonable_encoder(name)})

@router.put('/api/supermarket/{id}', tags=['Supermarket'])
async def update_supermarket(id: int, name: str = Query(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = SupermarketService(db).update_supermarket(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked updated'})

@router.delete('/api/supermarket/{id}', tags=['Supermarket'])
async def delete_supermarket(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = SupermarketService(db).delete_supermarket(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found supermarket'})
    return JSONResponse(status_code=200, content={'message': 'Supermarked deleted'})




@router.get('/api/category/all', tags=['Category'], response_model=Response)
async def get_categories(api_key: str = Depends(validate_api_key)):
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content={'message': 'Categories list', 'data':jsonable_encoder(result)})

@router.get('/api/category/{id}', tags=['Category'], response_model=Response)
async def get_category_by_id(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = CategoryService(db).get_category_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get category success', 'data':jsonable_encoder(result)})

@router.post('/api/category', tags=['Category'], response_model=Response)
async def create_category(name: str = Query(), api_key: str = Depends(validate_api_key)):
    db = Session()
    CategoryService(db).create_category(name)
    return JSONResponse(status_code=200, content={'message': 'category created', 'data':jsonable_encoder(name)})

@router.put('/api/category/{id}', tags=['Category'])
async def update_category(id: int, name: str = Query(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = CategoryService(db).update_category(id, name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category updated'})

@router.delete('/api/category/{id}', tags=['Category'])
async def delete_category(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = CategoryService(db).delete_category(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found category'})
    return JSONResponse(status_code=200, content={'message': 'Category deleted'})




@router.get('/api/product/all', tags=['Product'], response_model=Response)
async def get_products(api_key: str = Depends(validate_api_key)):
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content={'message': 'Products list', 'data':jsonable_encoder(result)})

@router.get('/api/product/{id}', tags=['Product'], response_model=Response)
async def get_product_by_id(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = ProductService(db).get_product_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get product success', 'data':jsonable_encoder(result)})

@router.post('/api/product', tags=['Product'], response_model=Response)
async def create_product(product: Product = Body(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = ProductService(db).create_product(product)
    return JSONResponse(status_code=200, content={'message': result})

@router.put('/api/product/{id}', tags=['Product'])
async def update_product(id: int, product: Product = Body(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = ProductService(db).update_product(id, product)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product updated'})

@router.delete('/api/product/{id}', tags=['Product'])
async def delete_product(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = ProductService(db).delete_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found product'})
    return JSONResponse(status_code=200, content={'message': 'Product deleted'})




@router.get('/api/user/all', tags=['User'], response_model=Response)
async def get_users(api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content={'message': 'Users list', 'data':jsonable_encoder(result)})

@router.get('/api/user/{id}', tags=['User'], response_model=Response)
async def get_user_by_id(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user', 'data':jsonable_encoder(result)})
    return JSONResponse(status_code=200, content={'message': 'Get user success', 'data':jsonable_encoder(result)})


@router.post('/api/user', tags=['User'], response_model=Response)
async def create_user(user: User = Body(), api_key: str = Depends(validate_api_key)):
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=200, content={'message': jsonable_encoder(user)})

@router.put('/api/product/{id}', tags=['User'])
async def update_user(id: int, password: str = Body(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).update_user(id, password)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user'})
    return JSONResponse(status_code=200, content={'message': 'User updated'})

@router.delete('/api/user/{id}', tags=['User'])
async def delete_user(id: int, api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).delete_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'Not found user'})
    return JSONResponse(status_code=200, content={'message': 'User deleted'})




@router.get('/api/compare/{name}', tags=['Over'], response_model=Response)
async def get_compare(name: str, api_key: str = Depends(validate_api_key)):
    return JSONResponse(status_code=200, content={'message': 'Building services'})

@router.post('/api/forgetPassword', tags=['Over'], response_model=Response)
async def forget_password(email: str = Query(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).post_forgetPassword(email)
    return JSONResponse(status_code=200, content={'message': jsonable_encoder(result)})

@router.post('/api/login', tags=['Over'], response_model=Response)
async def post_login(user: User = Body(), api_key: str = Depends(validate_api_key)):
    db = Session()
    result = UserService(db).post_login(user)
    return JSONResponse(status_code=200, content={'message': 'Get user success', 'data':jsonable_encoder(result)})
