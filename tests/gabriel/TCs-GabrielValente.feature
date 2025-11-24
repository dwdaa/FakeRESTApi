Funcionalidade: Gerenciamento de Autores na FakeRESTApi Como Engenheiro de QA, Quero validar as operações CRUD no recurso /Authors, Para garantir que o cadastro e recuperação de autores funcionem conforme o contrato da API.

Contexto Global:
    Dado que a URL base da API é "https://fakerestapi.azurewebsites.net/api/v1"
    E o recurso a ser testado é "/Authors"

1. POST (Create) - Criar Autor
Cenário: Criação bem-sucedida de um novo Autor
    Dado que possuo um payload de autor válido:

    {
      "id": 100,
      "idBook": 1,
      "firstName": "Gabriel",
      "lastName": "Valente"
    }

    Quando eu envio uma requisição POST para "/Authors"
    Então o Status Code da resposta deve ser 200 (ou 201 dependendo da API)
    E o corpo da resposta deve conter o "firstName" igual a "Gabriel"
    E o corpo da resposta deve conter o "lastName" igual a "Valente"

2. GET (Read List) - Listar Autores

Cenário: Leitura da lista completa de Autores
    Quando eu envio uma requisição GET para "/Authors"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve ser um array não nulo
    E os itens do array devem conter os campos idBook, firstName e lastName

3. GET (Read Specific) - Consultar Autor

Cenário: Leitura de um Autor específico pelo ID
    Dado que existe um Autor com ID 3
    Quando eu envio uma requisição GET para "/Authors/3"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve conter o campo "id" igual a 3

4. PUT (Update) - Atualizar Autor

Cenário: Atualização dos dados de um Autor existente
    Dado que desejo atualizar o Autor de ID 3 com os dados:
    {
      "id": 3,
      "idBook": 2,
      "firstName": "Autor",
      "lastName": "Atualizado"
    }
    
    Quando eu enviar uma requisição PUT para "/Authors/3"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve mostrar "firstName" igual a "Autor"
    E o corpo da resposta deve mostrar "lastName" igual a "Atualizado"

5. DELETE (Delete) - Excluir Autor

Cenário: Exclusão de um Autor existente
    Quando eu envio uma requisição DELETE para "/Authors/3"
    Então o Status Code da resposta deve ser 200