from uuid import uuid4

from werkzeug.security import check_password_hash

from app.entities.account import Account


def initialize_account_test():
    account = Account(
        id=uuid4().hex,
        email='test@test.com'
    )
    assert account.email == 'test@test.com'
    assert account.password is None
    assert account.is_active is True


def set_account_hashed_password_test(account):
    assert account.password is None

    pwd = 'test_password'
    account.set_password(pwd)
    hashed_pwd = account.password

    assert check_password_hash(hashed_pwd, pwd) is True


def check_account_correct_hashed_password_test(account):
    pwd = 'test_password'
    account.set_password(pwd)

    assert account.check_password(pwd) is True


def check_account_incorrect_password_test(account):
    pwd = 'test_password'
    wrong_pwd = '1234314'

    account.set_password(pwd)

    assert account.check_password(wrong_pwd) is False
