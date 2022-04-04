from app.api.dependencies.pagination_params import PaginationParams
from app.models.schemas.common.paginated import Paginated
from app.db.uow import UnitOfWork
from app.db.repositories.base_repository import BaseRepository
import sqlalchemy as sa
import app.models.entities as models
from app.models.schemas.team import ListOfTeamsInResponse, TeamInFilter


class TeamRepository(BaseRepository):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)

    async def find_teams(
        self, filters: TeamInFilter, pagination_params: PaginationParams
    ) -> Paginated[ListOfTeamsInResponse]:
        qb = sa.select(models.Team)

        if filters.name is not None:
            qb = qb.where(models.Team.name.ilike(f"%{filters.name}%"))
        if filters.description is not None:
            qb = qb.where(models.Team.description.ilike(f"%{filters.description}%"))

        qb = self.sort_query(qb, pagination_params.sort)

        result = await self.paginate_query(
            select=qb,
            model=ListOfTeamsInResponse,
            page=pagination_params.page,
            page_size=pagination_params.page_size,
        )
        return result
