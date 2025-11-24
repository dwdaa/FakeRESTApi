import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Users"
USER_ID = 1

def test_read_users_list_success():
    """Tópico 2: Teste GET (Read) - Recuperação de todos os recursos."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}")
    
    assert response.status_code == 200
    assert len(response.json()) > 0
    print("\n[GET] Recuperação da lista de usuários sucedida (200 OK).")

def test_read_specific_user_success():
    """Tópico 3: Teste GET (ID) - Recuperação de um recurso específico."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}/{USER_ID}")
    
    assert response.status_code == 200
    assert response.json()["id"] == USER_ID
    print("\n[GET] Recuperação de um usuário específico sucedida (200 OK).")