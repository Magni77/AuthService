from unittest.mock import Mock

import pytest

from app.use_cases.register import RegistrationUseCase


@pytest.fixture()
def account_repo(account):
    repo = Mock()
    repo.create.return_value = account
    return repo


def valid_account_is_created_test(account_repo):
    use_case = RegistrationUseCase(account_repo)

    request = Mock()
    request.email = 'test@test.com'
    request.password = 'testpwd'

    new_account = use_case.register(request)

    account_repo.create.assert_called_once_with(new_account)

    assert new_account.email == request.email
    assert new_account.check_password(request.password) is True
