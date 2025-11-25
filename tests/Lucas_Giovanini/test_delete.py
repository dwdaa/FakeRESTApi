import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
ENDPOINT_BOOKS = "/Books"
URL_COMPLETA = f"{BASE_URL}{ENDPOINT_BOOKS}"

def test_delete_exclui_livro_sucess():
    book_id = 1

    url = f"{URL_COMPLETA}/{book_id}"
    response = requests.delete(url)
    
    assert response.status_code == 200, f"era status 200, mas recebeu {response.status_code}"
    
    print("\n[delete_sucesso] exclusão de livro realizada com sucesso:", response.status_code)