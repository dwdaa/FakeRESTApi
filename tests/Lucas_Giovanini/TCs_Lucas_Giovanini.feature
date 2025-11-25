Cenário: GET - Leitura da lista completa de Livros
  Dado que a URL do recurso é "/Books"
  Quando eu envio uma requisição GET para "/Books"
  Então o Status Code da resposta deve ser 200
  E o corpo da resposta deve ser um array não vazio
  E os itens do array devem conter os campos 'id' e 'title'

Cenário: GET - Leitura de um Livro específico pelo ID
  Dado que a URL do recurso é "/Books/1"
  Quando eu envio uma requisição GET para "/Books/1"
  Então o Status Code da resposta deve ser 200
  E o corpo da resposta deve conter o campo "id" igual a 1
  E o corpo da resposta deve conter os detalhes do livro

Cenário: POST - Criação bem-sucedida de um novo Livro
  Dado que a URL do recurso é "/Books"
  E que possuo um payload de livro válido com o título "como testar uma api"
  Quando eu envio uma requisição POST para "/Books"
  Então o Status Code da resposta deve ser 200
  E o corpo da resposta deve conter o "title" igual a "como testar uma api"
  E o campo "pageCount" deve ser igual a 244

Cenário: PUT - Atualização dos dados de um Livro existente
  Dado que desejo atualizar o Livro de ID 1
  E que possuo o payload de atualização com "title" igual a "como testar uma api - 2.0"
  Quando eu envio uma requisição PUT para "/Books/1" com o payload
  Então o Status Code da resposta deve ser 200
  E o corpo da resposta deve mostrar "title" igual a "como testar uma api - 2.0"
  E o campo "pageCount" deve ser igual a 320

Cenário: DELETE - Exclusão de um Livro existente
  Dado que a URL do recurso é "/Books/1"
  Quando eu envio uma requisição DELETE para "/Books/1"
  Então o Status Code da resposta deve ser 200