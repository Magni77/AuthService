from unittest.mock import Mock

import pytest

from app.use_cases.authenticate import AuthUseCase

USER_DATA = {
        'email': 'test@test.com',
        'password': '1231'
    }
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
        ".eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJwYXNzd29yZCI6IjEyMzEifQ" \
        ".TN_ICNqQIPGZ154I1mwFRZHTo7ENTUmPUfksL1BPipE"


@pytest.fixture()
def jwt_gateway():
    return Mock(
        decode=Mock(return_value=USER_DATA),
        generate=Mock(return_value=TOKEN)
    )


def user_auth_with_jwt_token_test(
        account_repo: Mock, jwt_gateway: Mock, account_with_pwd):

    use_case = AuthUseCase(account_repo, jwt_gateway)

    account = use_case.auth(TOKEN)

    assert account is account_with_pwd

    jwt_gateway.decode.assert_called_once_with(TOKEN)
    account_repo.find.assert_called_once_with({'email': USER_DATA['email']})


def user_can_auth_with_correct_credentials_test(
        account_repo: Mock, jwt_gateway: Mock,
        login_request: Mock, account_with_pwd):

    use_case = AuthUseCase(account_repo, jwt_gateway)
    token = use_case.login(login_request)

    assert token is TOKEN
    account_repo.find.assert_called_once_with({'email': USER_DATA['email']})


def user_can_not_auth_with_incorrect_credentials_test(
        account_repo: Mock, jwt_gateway: Mock, account_with_pwd):

    request = Mock()
    request.email = 'test@test.com'
    request.password = '1232221'

    use_case = AuthUseCase(account_repo, jwt_gateway)
    account = use_case.login(request)

    assert account is None
    account_repo.find.assert_called_once_with({'email': USER_DATA['email']})
