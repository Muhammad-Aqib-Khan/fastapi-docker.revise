from fastapi.testclient import TestClient
from class01.main import app

def test_root_path():
    client = TestClient(app)  # Corrected line
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Welcome to my API" }

def test_piaic_client():
    client = TestClient(app)  # Corrected line
    response = client.get("/piaic/")
    assert response.status_code == 200  # Fixed the attribute 'status' to 'status_code'
    assert response.json() ==  {"organization ":  "Welcome to the PIAIC API"}
