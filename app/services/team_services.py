from app.api.dependencies.pagination_params import PaginationParams
from app.models.entities.team import Team
from app.models.schemas.team import ListOfTeamsInResponse, TeamInCreate, TeamInFilter
from app.db.repositories.team_repository import TeamRepository


class TeamServices:
    def __init__(self, repo: TeamRepository):
        self.repo = repo

    async def create(self, team: TeamInCreate) -> ListOfTeamsInResponse:
        team_entity = Team(**team.__dict__)
        result = await self.repo.add(team_entity)

        return ListOfTeamsInResponse.from_orm(result)

    async def get_all(self, filters: TeamInFilter, pagination_params: PaginationParams):
        result = await self.repo.find_teams(filters, pagination_params)
        return result
