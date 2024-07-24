import unittest
from flask import Flask
from flask.testing import FlaskClient
from server.api.admin import admin_blueprint


class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(admin_blueprint)
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post(
            "/api/admin/users", json={"email": "test@example.com", "password": "password", "roleId": 1})
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data

    def test_get_users(self):
        response = self.client.get("/api/admin/users")
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data

    def test_delete_user(self):
        response = self.client.delete("/api/admin/users/1")
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data

    def test_update_user(self):
        response = self.client.put("/api/admin/users/1", json={
                                   "username": "new_username", "email": "new_email@example.com", "roleId": 2})
        self.assertEqual(response.status_code, 200)
        # Add more assertions to validate the response data


if __name__ == "__main__":
    unittest.main()
