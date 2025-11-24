import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/CoverPhotos"
COVERPHOTO_ID = 1

def test_delete_book_cover_photo_success():
    """Tópico 5: Teste DELETE (Delete) - Exclusão de um recurso existente."""
    
    response = requests.delete(f"{BASE_URL}{RESOURCE}/{COVERPHOTO_ID}")
    
    assert response.status_code == 200
    
    print(f"[DELETE] Exclusão da capa do livro {COVERPHOTO_ID} sucedida (200 OK).")
    