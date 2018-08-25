import json

from bottle import route, response, request, run, abort

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

    account = use_case.register(data)

    return json.dumps({'email': account.email, 'id': account.id, 'info': 'created'})


@route('/login', method='POST')
def login():
    response.headers['Content-Type'] = 'application/json'

    use_case = AuthUseCase(repository, JwtGateway())
    data = RegisterRequest(**request.json)

    auth_response = use_case.login(data)
    if auth_response:
        return json.dumps({'token': auth_response})
    abort(401, 'Access denied')


run(host='localhost', port=8081, debug=True, reloader=True)
