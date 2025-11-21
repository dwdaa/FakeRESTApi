import requests
BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Activities"

def test_create_activity_success():
    """Tópico 1: Teste POST (Create) - Criação de um novo recurso."""
    
  
    payload = {
        "id": 0, 
        "title": "Atividade Criada para o Trabalho",
        "dueDate": "2025-12-01T10:00:00.000Z", 
        "completed": False
    }
    
    response = requests.post(f"{BASE_URL}{RESOURCE}", json=payload)
    
    assert response.status_code == 200
    data = response.json()   
    
    assert data.get('title') == payload['title']  
    
    assert 'id' in data and data.get('id') is not None
    
    print("\n[POST] Atividade criada com sucesso (200 OK).")