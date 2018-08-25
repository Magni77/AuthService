from datetime import datetime
from uuid import uuid4

import pytest

from app.entities.account import Account
from app.repositories.mem_account_repo import MemoryAccountRepository

id_1 = uuid4()
id_2 = uuid4()


@pytest.fixture()
def accounts():
    return [
        Account(
            id=id_1,
            email='test@test.com'
        ),
        Account(
            id=id_2,
            email='test2@test.com'
        ),
    ]


def repository_list_without_parameters_test(accounts):
    repo = MemoryAccountRepository(accounts)

    assert repo.find() == accounts


def repository_list_with_filters_unknown_key_test(accounts):
    repo = MemoryAccountRepository(accounts)

    with pytest.raises(AttributeError):
        repo.get(filters={'name': 'aname'})


def repository_list_with_filters_unknown_operator_test(accounts):
    repo = MemoryAccountRepository(accounts)

    with pytest.raises(ValueError):
        repo.get(filters={'author__in': [20, 30]})


def repository_list_with_filters_test(accounts):
    repo = MemoryAccountRepository(accounts)

    assert accounts[0] in repo.find(filters={'id': 1})
    assert accounts[1] in repo.find(filters={'email': 'test2@test.com'})
    assert accounts[1] in repo.find(filters={'id': 2})

    # assert all(
    #     post in accounts for post in repo.get(
    #         filters={'created__lt': datetime(1995, 2, 22, 16, 10)}
    #     )
    # )
    # assert not repo.get(
    #         filters={'created__gt': datetime(1995, 2, 22, 16, 10)}
    #     )


def repository_get_with_id_test(accounts):
    repo = MemoryAccountRepository(accounts)
    account = repo.get(filters={'id': id_1})

    assert isinstance(account, Account)
    assert account.id == id_1
