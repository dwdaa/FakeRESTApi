import requests

BASE_URL = "https://fakerestapi.azurewebsites.net/api/v1"
ENDPOINT_BOOKS = "/Books"
URL_COMPLETA = f"{BASE_URL}{ENDPOINT_BOOKS}"

def test_put_editar_livro_sucess():
    livro_atualizado = {
        "id": 1,
        "title": "como testar uma api - 2.0",
        "description": "tutorial de como testar uma api - 2.0",
        "pageCount": 320,
        "excerpt": "hoje vamos aprender a testar uma api de uma nova maneira",
        "publishDate": "2025-12-05T00:00:00Z"
    }
    
    url = f"{URL_COMPLETA}/{livro_atualizado['id']}"
    response = requests.put(url, json=livro_atualizado)
    
    assert response.status_code == 200, f"era status 200, mas recebeu {response.status_code}"
    
    livro_editado = response.json()
    
    assert livro_editado['title'] == livro_atualizado['title'], f"era pra ser o título '{livro_atualizado['title']}', mas foi '{livro_editado['title']}'"
    
    print("\n[put_sucesso] edição de livro realizada com sucesso:", response.status_code)