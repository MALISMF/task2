import random
import string

class UserFactory:
    @staticmethod
    def create_user():
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        login = ''.join(random.choices(string.ascii_lowercase, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        name = ''.join(random.choices(string.ascii_letters, k=10))
        email = f"{login}@example.com"
        return User(code, login, password, name, email)

    @staticmethod
    def create_users(n):
        return [UserFactory.create_user() for _ in range(n)]


class User:
    def __init__(self, code, login, password, name, email):
        self.code = code
        self.login = login
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(code={self.code}, login={self.login}, name={self.name}, email={self.email})"


if __name__ == "__main__":
    users = UserFactory.create_users(5)
    for user in users:
        print(user)

