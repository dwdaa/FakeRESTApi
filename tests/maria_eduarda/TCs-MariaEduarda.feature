
Funcionalidade: Testes CRUD no Recurso /Activities da FakeRESTApi
  Como Engenheira de QA,
  Eu quero validar o comportamento dos endpoints de Atividades,
  Para garantir a integridade dos dados na API.

  Contexto: 
    Dado que a URL base da API é "https://fakerestapi.azurewebsites.net/api/v1"
    E o recurso a ser testado é "/Activities"

  # 1. POST (Create)
  Cenário: Criação bem-sucedida de uma nova Atividade
    Dado que o payload de criação contém dados válidos
      | title | dueDate | completed |
      | Nova Tarefa | 2025-12-01T10:00:00.000Z | false |
    Quando eu envio uma requisição POST para "/Activities"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve conter o título "Nova Tarefa"

  # 2. GET (Read - Específico)
  Cenário: Leitura de uma Atividade existente pelo ID 5
    Dado que a Atividade com ID 5 existe
    Quando eu envio uma requisição GET para "/Activities/5"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve conter o campo "id" igual a 5

  # 3. GET (Read - Lista)
  Cenário: Leitura da lista geral de Atividades
    Quando eu envio uma requisição GET para "/Activities"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve ser uma lista não vazia

  # 4. PUT (Update)
  Cenário: Atualização completa de uma Atividade existente (ID 5)
    Dado que a Atividade com ID 5 será atualizada
      | title | completed |
      | Título Atualizado | true |
    Quando eu envio uma requisição PUT para "/Activities/5"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve ter o campo "completed" igual a true

  # 5. DELETE (Delete)
  Cenário: Exclusão de uma Atividade existente (ID 5)
    Quando eu envio uma requisição DELETE para "/Activities/5"
    Então o Status Code da resposta deve ser 200
    E o corpo da resposta deve ser vazio (sem conteúdo)