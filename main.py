import random
import string
import unittest

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


class Test(unittest.TestCase):

    def test_create_user(self):
        user = UserFactory.create_user()
        self.assertIsInstance(user, User)
        self.assertEqual(len(user.code), 6)
        self.assertTrue(user.code.isalnum())
        self.assertEqual(len(user.login), 8)
        self.assertTrue(user.login.islower())
        self.assertEqual(len(user.password), 10)
        self.assertTrue(all(c.isalnum() for c in user.password))
        self.assertEqual(len(user.name), 10)
        self.assertTrue(user.name.isalpha())
        self.assertEqual(user.email, f"{user.login}@example.com")

    def test_create_users(self):
        users = UserFactory.create_users(5)
        self.assertEqual(len(users), 5)
        for user in users:
            self.assertIsInstance(user, User)
            self.test_create_user()

if __name__ == '__main__':
    unittest.main()

