from fastapi import APIRouter, Body, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.db.database import Session
from app.api.interfaces.interfaces import Response, User
from app.services.user import UserService
from dependencies import validate_api_key


over = APIRouter(
    prefix="/api",
    tags=["Api"],
    dependencies=[Depends(validate_api_key)]
)


@over.get('/compare/{name}', response_model=Response)
async def get_compare(name: str):
    return JSONResponse(status_code=200, content={'message': 'Building services'})

@over.post('/forgetPassword', response_model=Response)
async def forget_password(email: str = Query()):
    db = Session()
    result = UserService(db).post_forgetPassword(email)
    return JSONResponse(status_code=200, content={'message': jsonable_encoder(result)})

@over.post('/login', response_model=Response)
async def post_login(user: User = Body()):
    db = Session()
    result = UserService(db).post_login(user)
    return JSONResponse(status_code=200, content={'message': 'Get user success', 'data':jsonable_encoder(result)})
