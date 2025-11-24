import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
RESOURCE = "/CoverPhotos"

def test_create_cover_photos_success():
    # Tópico 1: Teste POST (Create) - Criação de um novo recurso.
    new_cover_photo = {
        "id": 1,
        "idBook": 1,
        "url": "https://example.com/cover_photo.jpg",
    }
    response = requests.post(f"{BASE_URL}{RESOURCE}", json=new_cover_photo)
    assert response.status_code == 200
    data = response.json()

    print(data)

    assert data['id'] == new_cover_photo['id']
    assert data['idBook'] == new_cover_photo['idBook']
    assert data['url'] == new_cover_photo['url']
    print(f"[POST] Criação da capa do livro {data['id']} sucedida (200 OK).")