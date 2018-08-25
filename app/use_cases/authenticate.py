

class AuthUseCase:

    def __init__(self, repository, jwt_gateway):
        self.repository = repository
        self.jwt_gateway = jwt_gateway

    def auth(self, token):
        user_data = self.jwt_gateway.decode(token)
        account = self.repository.get({'email': user_data['email']})

        if account:
            return account
        return None

    def login(self, request):
        account = self.repository.get({'email': request.email})
        if account:
            is_pwd_correct = account.check_password(request.password)
            if is_pwd_correct:
                return self.jwt_gateway.generate(
                    {
                        'email': request.email,
                        'password': request.password
                    }
                )
        return None

# TODO Consider changing jwt_gateway to JWT class and pass object to auth method
