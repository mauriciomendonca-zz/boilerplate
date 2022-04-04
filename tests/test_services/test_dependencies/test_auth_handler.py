from time import time
import jwt
from pytest_mock import MockerFixture
from app.models.schemas.access_token import AccessTokenResponse
from app.services.dependencies.auth.auth_handler import sign_jwt, decode_jwt

expected_username = "user"
expected_role = "user"
jwt_secret = "secret"
jwt_algorithm = "HS256"
jwt_seconds_to_expire = 3600


def test_sign_jwt(mocker: MockerFixture):
    mocker.patch(
        "app.services.dependencies.auth.auth_handler.config.JWT_SECRET", jwt_secret
    )
    mocker.patch(
        "app.services.dependencies.auth.auth_handler.config.JWT_ALGORITHM",
        jwt_algorithm,
    )
    current_time = time()
    mocker.patch(
        "app.services.dependencies.auth.auth_handler.time", return_value=current_time
    )

    expected_token = jwt.encode(
        {
            "username": expected_username,
            "role": expected_role,
            "exp": int(current_time) + jwt_seconds_to_expire,
        },
        jwt_secret,
        jwt_algorithm,
    )

    access_token_response = sign_jwt(
        username=expected_username,
        role=expected_role,
        seconds_to_expire=jwt_seconds_to_expire,
    )
    assert access_token_response == AccessTokenResponse(
        access_token=expected_token,
        username=expected_username,
        role=expected_role,
    )


def test_decode_jwt(mocker: MockerFixture):
    mocker.patch(
        "app.services.dependencies.auth.auth_handler.config.JWT_SECRET", "secret"
    )
    mocker.patch(
        "app.services.dependencies.auth.auth_handler.config.JWT_ALGORITHM", "HS256"
    )
    current_time = time()

    decoded_jwt = decode_jwt(
        jwt.encode(
            {
                "username": expected_username,
                "role": expected_role,
                "exp": int(current_time) + jwt_seconds_to_expire,
            },
            jwt_secret,
            jwt_algorithm,
        )
    )
    assert decoded_jwt == {
        "username": expected_username,
        "role": expected_role,
        "exp": int(current_time) + jwt_seconds_to_expire,
    }
