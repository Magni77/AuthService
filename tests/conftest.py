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
