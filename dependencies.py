import os

from dotenv import load_dotenv
from fastapi import HTTPException, Header


async def validate_api_key(api_key: str = Header()):
    load_dotenv()
    if api_key != os.getenv('API-KEY'):
        raise HTTPException(status_code = 400, detail = "API Key inválida")