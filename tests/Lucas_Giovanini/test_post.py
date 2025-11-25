import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
ENDPOINT_BOOKS = "/Books"
URL_COMPLETA = f"{BASE_URL}{ENDPOINT_BOOKS}"

def test_post_registrar_livro_sucess():
    novo_livro = {
        "id": 0,
        "title": "como testar uma api",
        "description": "tutorial de como testar uma api",
        "pageCount": 244,
        "excerpt": "hoje vamos aprender a testar uma api",
        "publishDate": "2025-11-24T00:00:00Z"
    }
    
    response = requests.post(URL_COMPLETA, json=novo_livro)
    
    assert response.status_code == 200, f"era status 200, mas recebeu {response.status_code}"
    
    livro_criado = response.json()
    
    assert livro_criado['title'] == novo_livro['title'], f"Esperava título '{novo_livro['title']}', mas recebeu '{livro_criado['title']}'"
    
    print("\n[post_sucesso] criação de livro com sucesso:", response.status_code)
