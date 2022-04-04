from fastapi import APIRouter, Depends
from app.models.schemas.access_token import AccessTokenInCreate, AccessTokenResponse
from app.services.dependencies.auth.auth_bearer import JWTBearer
from app.services.auth_service import AuthService

router = APIRouter()


@router.post(
    "/token",
    response_model=AccessTokenResponse,
    name="Auth: Create token",
    dependencies=[Depends(JWTBearer(roles=["admin"]))],
)
def create(
    token_req: AccessTokenInCreate, auth_service: AuthService = Depends(AuthService)
) -> AccessTokenResponse:
    response = auth_service.create(token_req)

    return response
