import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Authors"
AUTHOR_ID = 3

def test_create_author_success():
    """Tópico 1: Teste POST (Create)"""
    new_author = {
        "id": AUTHOR_ID,
        "idBook": 10,
        "firstName": "Test",
        "lastName": "QA"
    }
    
    response = requests.post(f"{BASE_URL}{RESOURCE}", json=new_author)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['firstName'] == new_author['firstName']
    assert data['lastName'] == new_author['lastName']
    
    print(f"[POST] Criação do autor {data['firstName']} {data['lastName']} sucedida (200 OK).")