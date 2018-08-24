from werkzeug.security import generate_password_hash, check_password_hash


class Account:
    def __init__(self, id, email, password=None):
        self.id = id
        self.email = email
        self.password = password
        self.is_active = True

    def set_password(self, password: str):
        self.password = generate_password_hash(password, "sha256")

    def check_password(self, password: str):
        return check_password_hash(self.password, password)
