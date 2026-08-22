from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_get_tasks_empty():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
