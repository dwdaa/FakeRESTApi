import requests
BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Activities"
ACTIVITY_ID = 5 

def test_delete_activity_success():
    """Tópico 4: Teste DELETE (Delete) - Exclusão de uma atividade."""

    response = requests.delete(f"{BASE_URL}{RESOURCE}/{ACTIVITY_ID}")
   
    assert response.status_code == 200
    
    assert response.text == "" or response.json() == {}
    
    print(f"\n[DELETE] Atividade {ACTIVITY_ID} excluída com sucesso (200 OK).")