import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Users"

def test_create_user_success():
    # Tópico 1: Teste POST (Create) - Criação de um novo recurso.
    new_user = {
        "id": 1,
        "userName": "username",
        "password": "password123",
    }
    response = requests.post(f"{BASE_URL}{RESOURCE}", json=new_user)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == new_user['id']
    assert data['userName'] == new_user['userName']
    assert data['password'] == new_user['password']
    print(f"[POST] Criação do usuário {data['id']} sucedida (200 OK).")