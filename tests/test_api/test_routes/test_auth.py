import pytest
from pytest_mock import MockerFixture
from httpx import AsyncClient
from starlette import status

pytestmark = pytest.mark.asyncio

create_token_data = {"username": "user", "role": "user"}


async def test_cannot_create_token_if_not_logged(
    client: AsyncClient, mocker: MockerFixture
):
    mocker.patch("app.services.auth_service.AuthService.create", return_value=None)

    response = await client.post("/api/auth/token", json=create_token_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize("role", ["invalid_role"])
async def test_cannot_create_token_if_not_authorized(
    authorized_client: AsyncClient, mocker: MockerFixture
):
    mocker.patch("app.services.auth_service.AuthService.create", return_value=None)

    response = await authorized_client.post("/api/auth/token", json=create_token_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize("role", ["admin"])
async def test_create_token(authorized_client: AsyncClient, mocker: MockerFixture):
    mocker.patch(
        "app.services.auth_service.AuthService.create",
        return_value={**create_token_data, "access_token": "token"},
    )

    response = await authorized_client.post("/api/auth/token", json=create_token_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {**create_token_data, "access_token": "token"}
