from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_addition():
    x_test = 100
    y_test = 99
    expected_x_plus_y = x_test + y_test
    response = client.get(f"/add?x={x_test}&y={y_test}")
    assert response.status_code == 200
    assert response.json() == {
        "data": expected_x_plus_y,
        "message": "success"
    }