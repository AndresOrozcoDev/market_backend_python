import uvicorn

from fastapi import FastAPI, Depends

from routers.user import user
from routers.over import over
from routers.product import product
from routers.category import category
from routers.supermarket import supermarket
from config.database import engine, Base
from dependencies import validate_api_key
from app.utils.middlewares.error_handle import ErrorHandler


app = FastAPI(
    dependencies=[Depends(validate_api_key)],
    title='Market project backend',
    version='1.0.0'
)


@app.get("/")
async def root():
    return {"message": "Welcome to Market Backend Project with Python and FastAPI!. Please add '/docs' to url"}


app.add_middleware(ErrorHandler)

app.include_router(supermarket)
app.include_router(category)
app.include_router(product)
app.include_router(user)
app.include_router(over)

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)