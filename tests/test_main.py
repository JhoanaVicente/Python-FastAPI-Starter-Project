import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to my FastAPI application!"})
