import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Authors"
AUTHOR_ID = 3

def test_update_author_success():
    """Tópico 4: Teste PUT (Update)"""
    updated_author = {
        "id": AUTHOR_ID,
        "idBook": 10,
        "firstName": "Nome",
        "lastName": "Editado"
    }
    
    response = requests.put(f"{BASE_URL}{RESOURCE}/{AUTHOR_ID}", json=updated_author)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['firstName'] == updated_author['firstName']
    assert data['lastName'] == updated_author['lastName']
    
    print(f"[PUT] Atualização do autor {data['firstName']} {data['lastName']} sucedida (200 OK).")
