from pytest_mock import MockerFixture
from app.models.schemas.access_token import AccessTokenInCreate, AccessTokenResponse
from app.services.auth_service import AuthService


def test_sign_jwt(mocker: MockerFixture):
    username = "user"
    role = "user"
    access_token = "token"

    mocker.patch(
        "app.services.auth_service.sign_jwt",
        return_value=AccessTokenResponse(
            username=username, role=role, access_token=access_token
        ),
    )

    response = AuthService().create(AccessTokenInCreate(username=username, role=role))
    assert response == AccessTokenResponse(
        username=username, role=role, access_token=access_token
    )
