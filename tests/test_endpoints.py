import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestEndpoints(unittest.TestCase):

    def test_read_item(self):
        response = client.get("/items/1")
        self.assertEqual(response.status_code, 404)  # No hay ítem con id 1 inicialmente

    def test_create_item(self):
        response = client.post("/items/", json={"name": "Test Item", "price": 10.0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test Item")
        self.assertEqual(response.json()["price"], 10.0)

        # Verifica que el ítem puede ser leído
        response = client.get("/items/Test Item")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Test Item")
        self.assertEqual(response.json()["price"], 10.0)
