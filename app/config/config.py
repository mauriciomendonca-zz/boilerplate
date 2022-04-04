import logging
import os
from typing import List
from databases import DatabaseURL

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

env_file = ".env"
config = Config(env_file)

API_PREFIX = "/api"

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI application boilerplate")
VERSION = "0.1.1"

DEBUG: bool = config("DEBUG", cast=bool, default=False)

POSTGRES_USER: str = config("POSTGRES_USER")
POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
POSTGRES_HOST: str = config("POSTGRES_HOST")
POSTGRES_DB: str = config("POSTGRES_DB")
DATABASE_URL: DatabaseURL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"

MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

JWT_ALGORITHM = "HS256"
JWT_SECONDS_TO_EXPIRE = config(
    "JWT_SECONDS_TO_EXPIRE", cast=int, default=365 * 24 * 3600
)
JWT_SECRET = config("JWT_SECRET", cast=str)

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")
