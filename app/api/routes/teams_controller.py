from app.models.schemas.common.paginated import Paginated
from app.api.dependencies.pagination_params import PaginationParams
from app.services.dependencies.auth.auth_bearer import JWTBearer
from app.services.team_services import TeamServices
from app.api.dependencies.team import get_team_service
from fastapi import APIRouter, Depends

from app.models.schemas.team import ListOfTeamsInResponse, TeamInCreate, TeamInFilter

router = APIRouter()


@router.post(
    "",
    response_model=ListOfTeamsInResponse,
    name="Teams: create new team",
    dependencies=[Depends(JWTBearer(roles=["admin", "user"]))],
)
async def create(
    team: TeamInCreate,
    team_service: TeamServices = Depends(get_team_service),
) -> ListOfTeamsInResponse:
    result = await team_service.create(team)

    return result


@router.get(
    "",
    response_model=Paginated[ListOfTeamsInResponse],
    name="Teams: get all teams",
)
async def get_all(
    filters: TeamInFilter = Depends(),
    pagination_params: PaginationParams = Depends(),
    team_service: TeamServices = Depends(get_team_service),
) -> Paginated[ListOfTeamsInResponse]:
    result = await team_service.get_all(filters, pagination_params)

    return result
