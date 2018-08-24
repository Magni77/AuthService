import jwt


class JwtGateway:
    SECRET = 'secret'

    def decode(self, token):
        return jwt.decode(token, self.SECRET, algorithm='HS256')

    def generate(self, data):
        return jwt.encode(data, self.SECRET, algorithm='HS256')
