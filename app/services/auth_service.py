from app.models.schemas.access_token import AccessTokenInCreate, AccessTokenResponse
from app.services.dependencies.auth.auth_handler import sign_jwt


class AuthService:
    def create(self, access_token_info: AccessTokenInCreate) -> AccessTokenResponse:
        result = sign_jwt(access_token_info.username, access_token_info.role)
        return result
