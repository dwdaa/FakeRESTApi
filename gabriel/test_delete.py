import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Authors"
AUTHOR_ID = 3

def test_delete_author_success():
    """Tópico 5: Teste DELETE"""
    response = requests.delete(f"{BASE_URL}{RESOURCE}/{AUTHOR_ID}")
    
    assert response.status_code == 200
    
    print(f"[DELETE] Exclusão do autor {AUTHOR_ID} sucedida (200 OK).")