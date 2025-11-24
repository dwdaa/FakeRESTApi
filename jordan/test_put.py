import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/CoverPhotos"

def test_update_cover_photos_success():
    # Tópico 3: Teste PUT (Update) - Atualização de um recurso existente.
    updated_cover_photo = {
        "id": 1,
        "idBook": 1,
        "url": "https://example.com/updated_cover_photo.jpg",
    }
    response = requests.put(f"{BASE_URL}{RESOURCE}/1", json=updated_cover_photo)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == updated_cover_photo['id']
    assert data['idBook'] == updated_cover_photo['idBook']
    assert data['url'] == updated_cover_photo['url']
    print(f"[PUT] Atualização da capa do livro {data['id']} sucedida (200 OK).")
