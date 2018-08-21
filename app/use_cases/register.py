from uuid import uuid4

from app.entities.account import Account


class RegistrationUseCase:

    def __init__(self, repository):
        self.repo = repository

    def register(self, request):
        account = Account(
            id=uuid4().hex,
            email=request.email
        )
        account.set_password(request.password)
        self.repo.create(account)

        return account
