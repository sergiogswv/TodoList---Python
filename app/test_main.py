from starlette.testclient import TestClient
from .main import app

client = TestClient(app)

def test_main_greeting():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"msg": "Hello World"}

def test_route_getAllTasks():
  response = client.get("/task")
  assert response.status_code == 200
  assert response.json() == [{"id": 1, "name": "Rick", "finished": "false"}, {"id": 2, "name": "Morty", "finished": "true"}]

def test_route_getAllTasksError():
  response = client.get("/task/5")
  assert response.status_code == 404
  assert response.json() == {"detail": "Task not found"}

def test_route_postNewTask():
  response = client.post("/task", json={"id": 3, "name": "Summer", "finished": "false"})
  assert response.status_code == 200
  assert response.json() == {"id": 3, "name": "Summer", "finished": "false"}

def test_route_postNewTaskError():
  response = client.post("/task", json={"id": "3", "name": "", "finished": "false"})
  assert response.status_code == 400
  assert response.json() == {"detail": "The field name is empty"}

def test_route_deleteTask():
  response = client.delete('/task/1',)
  assert response.status_code == 200
  assert response.json() == {"detail": "The task 1 was eliminated successfuly"}

def test_route_deleteTaskError():
  response = client.delete('/task/1000')
  assert response.status_code == 404
  assert response.json() == {"detail": "Task not found"}

def test_route_updateTask():
  response = client.put('/task/1', json={"id": "1", "name": "Morty - v2.0", "finished": "true"})
  assert response.status_code == 200
  assert response.json() == {'detail': 'The task 1 was updated successfuly'}

def test_route_updateTaskError():
  response = client.put('/task/100', json={"id": "100", "name": "Morty - v2.0", "finished": "true"})
  assert response.status_code == 404
  assert response.json() == {'detail': 'Task not found'}