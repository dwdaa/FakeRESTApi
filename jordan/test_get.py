import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/CoverPhotos"
COVERPHOTO_ID = 1

def test_list_book_cover_photos_success():
    """Tópico 3: Teste GET (Read) - Leitura da lista de capas de livros."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}")
    
    assert response.status_code == 200
    data = response.json()
  
    assert len(data) > 0 
    
    print("\n[GET] Leitura da lista de capas de livros sucedida (200 OK).")

def test_read_specific_book_cover_photo_success():
    """Tópico 4: Teste GET (Read) - Leitura de capa de livro específica por ID."""
    
    response = requests.get(f"{BASE_URL}{RESOURCE}/{COVERPHOTO_ID}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['id'] == COVERPHOTO_ID
    
    print(f"[GET] Leitura da capa do livro {COVERPHOTO_ID} sucedida (200 OK).")