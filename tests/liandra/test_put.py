import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Users"

def test_update_user_success():
    # Tópico 4: Teste PUT (Update) - Atualização de um recurso existente.
    updated_user = {
        "id": 1,
        "userName": "updated_user",
        "password": "new_password123",
    }
    response = requests.put(f"{BASE_URL}{RESOURCE}/1", json=updated_user)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == updated_user['id']
    assert data['userName'] == updated_user['userName']
    assert data['password'] == updated_user['password']
    print(f"[PUT] Atualização do usuário {data['id']} sucedida (200 OK).")