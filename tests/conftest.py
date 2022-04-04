import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from app.services.dependencies.auth.auth_handler import sign_jwt

# environ["ENV"] = "test"


@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application

    return get_application()


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest.fixture
def authorization_prefix():
    return "Bearer"


@pytest.fixture
def username():
    return "Test User"


@pytest.fixture
def role():
    return "user"


@pytest.fixture
def token(username: str, role: str):
    return sign_jwt(
        username,
        role,
    ).access_token


@pytest.fixture
def authorized_client(
    client: AsyncClient, token: str, authorization_prefix: str
) -> AsyncClient:
    client.headers = {
        "Authorization": f"{authorization_prefix} {token}",
        **client.headers,
    }
    return client
