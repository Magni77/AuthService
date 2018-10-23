import json

from bottle import route, response, request, run, abort

from app.api.decorators import login_required
from app.api.requests import RegisterRequest
from app.gateways.jwt_gateway import JwtGateway
from app.repositories.mem_account_repo import MemoryAccountRepository
from app.use_cases.authenticate import AuthUseCase
from app.use_cases.register import RegistrationUseCase

repository = MemoryAccountRepository()


@route('/register', method='POST')
def register():
    response.headers['Content-Type'] = 'application/json'

    use_case = RegistrationUseCase(repository)
    data = RegisterRequest(**request.json)
    token_us = AuthUseCase(repository, JwtGateway())

    account = use_case.register(data)
    token, _ = token_us.login(data)
    if account:
        user_data = {'email': account.email, 'id': account.id}
        print(user_data)
        return json.dumps({'user': user_data, 'token': token})
    abort(400, json.dumps({'info': 'email already exists'}))


@route('/login', method='POST')
def login():
    response.headers['Content-Type'] = 'application/json'

    use_case = AuthUseCase(repository, JwtGateway())
    data = RegisterRequest(**request.json)
    token, account = use_case.login(data)

    if token:
        user_data = {'email': account.email, 'id': account.id}

        return json.dumps({'user': user_data, 'token': token})

    abort(401, 'Access denied')


@route('/accounts')
@login_required
def accounts(user):
    response.headers['Content-Type'] = 'application/json'
    response.content_type = 'application/json'

    accounts = repository.find()
    print(accounts)

    return json.dumps([{
        'id': account.id,
        'email': account.email
    } for account in accounts])


run(host='localhost', port=8081, debug=True, reloader=True)
