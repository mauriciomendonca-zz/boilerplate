import pytest
from pytest_mock import MockerFixture
from app.api.dependencies.pagination_params import PaginationParams
from app.db.repositories.team_repository import TeamRepository
from app.models.schemas.team import TeamInFilter
from tests.fake_uow import FakeUnitOfWork


pytestmark = pytest.mark.asyncio


async def test_find_teams(mocker: MockerFixture):
    expected_result = [{"id": 1, "name": "Team 1", "description": "description"}]

    # A consulta é executada de fato no paginate_query. Como não estamos
    # testando diretamente o SQLAlchemy, um mock é criado aqui
    mocker.patch(
        "app.db.repositories.team_repository.TeamRepository.paginate_query",
        mocker.AsyncMock(return_value=expected_result),
    )

    repo = TeamRepository(FakeUnitOfWork())
    result = await repo.find_teams(
        TeamInFilter(name="Team 1", description="description"), PaginationParams(1, 15, "id")
    )
    assert result == expected_result
