import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/Authors"
AUTHOR_ID = 3

def test_read_authors_list_success():
    """Tópico 2: Teste GET (Lista)"""
    response = requests.get(f"{BASE_URL}{RESOURCE}")
    
    assert response.status_code == 200
    data = response.json()
    
    # Verifica se é uma lista e se tem itens
    assert isinstance(data, list)
    assert len(data) > 0
    
    print("\n[GET] Leitura da lista de autores sucedida (200 OK).")

def test_read_specific_author_success():
    """Tópico 3: Teste GET (Específico)"""
    # CORREÇÃO: Adicionada a barra '/' antes do ID
    response = requests.get(f"{BASE_URL}{RESOURCE}/{AUTHOR_ID}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['id'] == AUTHOR_ID
    
    print(f"[GET] Leitura do autor {AUTHOR_ID} sucedida (200 OK).")