import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Users"
USER_ID = 1

def test_delete_user_success():
    """Tópico 5: Teste DELETE (Delete) - Exclusão de um recurso existente."""
    
    response = requests.delete(f"{BASE_URL}{RESOURCE}/{USER_ID}")
    
    assert response.status_code == 200
    
    print(f"[DELETE] Exclusão do usuário {USER_ID} sucedida (200 OK).")