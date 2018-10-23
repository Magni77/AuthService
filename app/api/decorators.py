from bottle import route, request, abort

from app.gateways.jwt_gateway import JwtGateway


def login_required(func):
    def login_wrapper(*args, **kwargs):
        token = request.headers.get('authorization')
        if not token:
            abort(401, 'Access denied')
        user_data = JwtGateway().decode(token)
        return func(user_data, *args, **kwargs)

    return login_wrapper
