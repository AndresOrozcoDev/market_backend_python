import uvicorn

from fastapi import FastAPI
from routes.routers import router
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler


app = FastAPI()

app.add_middleware(ErrorHandler)
app.include_router(router)
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)