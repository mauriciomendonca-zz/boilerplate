import pytest
from pytest_mock import MockerFixture
from app.api.dependencies.pagination_params import PaginationParams
from app.db.repositories.team_repository import TeamRepository
from app.models.entities.team import Team
from app.models.schemas.team import ListOfTeamsInResponse, TeamInCreate, TeamInFilter
from app.models.schemas.common.paginated import Paginated
from app.services.team_services import TeamServices
from tests.fake_uow import FakeUnitOfWork


pytestmark = pytest.mark.asyncio


async def test_create_team(mocker: MockerFixture):
    id = 1
    name = "team"
    description = "description"

    mocker.patch(
        "app.db.repositories.team_repository.TeamRepository.add",
        return_value=Team(id=id, name=name, description=description),
    )

    repo = TeamRepository(FakeUnitOfWork())
    service = TeamServices(repo)

    response = await service.create(TeamInCreate(name=name, description=description))
    assert response == ListOfTeamsInResponse(id=id, name=name, description=description)


async def test_get_teams(mocker: MockerFixture):
    teams = [
        Team(id=1, name="team1", description="description1"),
        Team(id=2, name="team2", description="description2"),
    ]

    response_value = Paginated(
        items=teams, total_items=len(teams), total_pages=1, current_page=1
    )

    mocker.patch(
        "app.db.repositories.team_repository.TeamRepository.find_teams",
        return_value=response_value,
    )

    repo = TeamRepository(FakeUnitOfWork())
    service = TeamServices(repo)

    response = await service.get_all(
        TeamInFilter(name=None, description=None), PaginationParams()
    )
    assert response == response_value
