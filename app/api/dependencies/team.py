from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.db.uow import UnitOfWork
from app.services.dependencies.get_db import get_session
from app.db.repositories.team_repository import TeamRepository
from app.services.team_services import TeamServices


async def get_team_service(
    session: AsyncSession = Depends(get_session),
) -> TeamServices:
    uow = UnitOfWork(session)
    repository = TeamRepository(uow)
    return TeamServices(repository)
