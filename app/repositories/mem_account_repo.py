from app.entities.account import Account
from app.repositories.account_repo import AccountsRepository


class MemoryAccountRepository(AccountsRepository):

    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        return getattr(
            getattr(element, key), operator
        )(value)

    def _search(self, filters):
        result = []
        result.extend(self._entries)

        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return result

    def find(self, filters=None):
        if not filters:
            return self._entries

        results = self._search(filters)

        return [Account_ for Account_ in results]

    def get(self, filters=None):
        if not filters:
            return None

        results = self._search(filters)

        if len(results) > 1:
            raise Exception('Get more than one value!')

        return results[0]

    def create(self, account: Account):
        self._entries.append(account)
