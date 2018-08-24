from unittest.mock import Mock
from uuid import uuid4

import pytest

from app.entities.account import Account


@pytest.fixture()
def account_id():
    return uuid4().hex


@pytest.fixture()
def account(account_id):
    return Account(
        id=account_id,
        email='test@test.com'
    )


@pytest.fixture()
def account_with_pwd(account_id):
    account = Account(
        id=account_id,
        email='test@test.com'
    )
    account.set_password('1231')
    return account


@pytest.fixture()
def account_repo(account, account_with_pwd):
    repo = Mock(
        create=Mock(return_value=account),
        find=Mock(return_value=account_with_pwd)
    )

    return repo


@pytest.fixture()
def login_request():
    request = Mock()
    request.email = 'test@test.com'
    request.password = '1231'
    return request
