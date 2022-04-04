import pytest
from pytest_mock import MockerFixture
from httpx import AsyncClient
from starlette import status
from fastapi.applications import FastAPI

pytestmark = pytest.mark.asyncio


created_team = {"id": 1, "name": "team", "description": "description"}


async def test_get_teams(client: AsyncClient, mocker: MockerFixture):
    mocker.patch(
        "app.services.team_services.TeamServices.get_all",
        return_value={
            "total_items": 1,
            "current_page": 1,
            "total_pages": 1,
            "items": [created_team],
        },
    )
    response = await client.get("/api/teams")
    rs_body = response.json()
    assert len(rs_body["items"]) == rs_body["total_items"]


async def test_create_team(authorized_client: AsyncClient, mocker: MockerFixture):
    mocker.patch(
        "app.services.team_services.TeamServices.create",
        return_value=created_team,
    )
    response = await authorized_client.post(
        "/api/teams",
        json={"name": "team", "description": "description"},
    )
    assert response.status_code == 200

    rs_body = response.json()
    assert rs_body["name"] == "team"


async def test_cannot_create_team_if_not_logged(
    client: AsyncClient, mocker: MockerFixture
):
    mocker.patch(
        "app.services.team_services.TeamServices.create",
        return_value=created_team,
    )
    response = await client.post(
        "/api/teams",
        json={"name": "test", "description": "test description"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize("role", ["invalid_role"])
async def test_cannot_create_team_if_not_authorized(
    authorized_client: AsyncClient, mocker: MockerFixture
):
    mocker.patch(
        "app.services.team_services.TeamServices.create",
        return_value=created_team,
    )
    response = await authorized_client.post(
        "/api/teams",
        json={"name": "test", "description": "test description"},
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
