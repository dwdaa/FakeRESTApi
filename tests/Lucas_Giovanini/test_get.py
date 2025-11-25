import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
ENDPOINT_BOOKS = "/Books"
URL_COMPLETA = f"{BASE_URL}{ENDPOINT_BOOKS}"

def test_get_todos_livros_sucess():
    response = requests.get(URL_COMPLETA)
    
    assert response.status_code == 200, f"era status 200, mas recebeu {response.status_code}"
    
    books = response.json()
    
    assert len(books) > 0, "a lista de livros está vazia."
    
    print("\n[get_sucesso] leitura de livros com sucesso:", response.status_code)

def test_get_livros_especificos_sucess():
    book_id = 1

    url = f"{URL_COMPLETA}/{book_id}"
    response = requests.get(url)
    
    assert response.status_code == 200, f"era status 200, mas recebeu {response.status_code}"
    
    book = response.json()
    
    assert book['id'] == book_id, f"era pro id do livro ser {book_id}, mas foi {book['id']}"
    
    print("\n[get_especifico_sucesso] leitura de livro específico com sucesso:", response.status_code)