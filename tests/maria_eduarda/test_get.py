import requests
BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Activities"
ACTIVITY_ID = 5 

def test_read_activities_list_success():
    """Tópico 2.1: Teste GET (Read) - Leitura da lista de atividades."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}")
    
    assert response.status_code == 200
    data = response.json()
  
    assert len(data) > 10 
    
    print("\n[GET] Leitura da lista de atividades sucedida (200 OK).")

def test_read_specific_activity_success():
    """Tópico 2.2: Teste GET (Read) - Leitura de atividade específica por ID."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}/{ACTIVITY_ID}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['id'] == ACTIVITY_ID
    
    print(f"[GET] Leitura da atividade {ACTIVITY_ID} sucedida (200 OK).")