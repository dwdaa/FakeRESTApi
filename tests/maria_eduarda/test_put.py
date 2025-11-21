

import requests
BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Activities"
ACTIVITY_ID = 5 

def test_update_activity_success():
    """Tópico 3: Teste PUT (Update) - Atualização completa de uma atividade."""
    payload = {
        "id": ACTIVITY_ID,
        "title": "TÍTULO ATUALIZADO PELO PUT", 
        "dueDate": "2025-10-20T10:00:00.000Z",
        "completed": True # Marcando como completa
    }
    
    response = requests.put(f"{BASE_URL}{RESOURCE}/{ACTIVITY_ID}", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data.get('title') == payload['title']
    assert data.get('completed') == True
    
    print(f"\n[PUT] Atividade {ACTIVITY_ID} atualizada com sucesso (200 OK).")