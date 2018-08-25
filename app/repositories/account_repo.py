from abc import ABC, abstractmethod, ABCMeta

from app.entities.account import Account


class AccountsRepository(metaclass=ABCMeta):

    @abstractmethod
    def find(self, id):
        raise NotImplementedError

    @abstractmethod
    def create(self, account: Account):
        raise NotImplementedError
