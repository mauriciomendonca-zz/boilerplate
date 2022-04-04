from fastapi.param_functions import Depends
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from app.services.dependencies.auth.auth_bearer import JWTBearer
from app.services.dependencies.auth.auth_handler import sign_jwt

pytestmark = pytest.mark.asyncio


def test_verify_jwt_valid():
    token = sign_jwt("user").access_token
    result = JWTBearer().verify_jwt(token)
    assert result is True


def test_verify_jwt_invalid():
    result = JWTBearer().verify_jwt("invalid_jwt")
    assert result is False


async def test_auth_bearer(app: FastAPI, authorized_client: AsyncClient):
    @app.get("/test_protected_route", dependencies=[Depends(JWTBearer(roles=["user"]))])
    def test_protected_route():
        return {"success": True}

    response = await authorized_client.get("/test_protected_route")
    assert response.status_code == 200
    assert response.json() == {"success": True}


async def test_auth_bearer_invalid_scheme(app: FastAPI, client: AsyncClient):
    @app.get("/test_protected_route", dependencies=[Depends(JWTBearer(roles=["user"]))])
    def test_protected_route():
        return {"success": True}

    client.headers = {
        "Authorization": "InvalidScheme invalid_jwt",
        **client.headers,
    }

    response = await client.get("/test_protected_route")
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid authentication credentials"}


async def test_auth_bearer_invalid_scheme_no_auto_error(
    app: FastAPI, client: AsyncClient
):
    @app.get(
        "/test_protected_route",
        dependencies=[Depends(JWTBearer(roles=["user"], auto_error=False))],
    )
    def test_protected_route():
        return {"success": True}

    client.headers = {
        "Authorization": "InvalidScheme invalid_jwt",
        **client.headers,
    }

    response = await client.get("/test_protected_route")
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid authorization code"}
