import jwt

from app.gateways.jwt_gateway import JwtGateway

USER_DATA = {
        'email': 'test@test.com',
        'password': '1231'
    }
SECRET = 'secret'
TOKEN = jwt.encode(USER_DATA, SECRET, algorithm='HS256').decode('utf8')


def can_decode_token_test():
    jwt_gw = JwtGateway
    jwt_gw.SECRET = SECRET

    user_data = JwtGateway().decode(TOKEN)

    assert user_data == USER_DATA


def can_generate_token_test():
    jwt_gw = JwtGateway()
    jwt_gw.SECRET = SECRET

    token = jwt_gw.generate(USER_DATA)

    assert token == TOKEN
