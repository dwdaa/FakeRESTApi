Plano de Testes: API de CoverPhotos

Ambiente: https://fakerestapi.azurewebsites.net/api/v1

01. Criação de Recurso (POST)
Identificador: TC-CREATE-001 Descrição: Verificar a criação de uma nova capa de livro com payload válido.
    Endpoint: POST /CoverPhotos
    Payload de Envio (JSON):

    {
        "id": 1,
        "idBook": 1,
        "url": "https://example.com/cover_photo.jpg"
    }

    Procedimento:
        Enviar a requisição POST com o corpo acima.
        Capturar a resposta.

    Critérios de Aceite:
        Status Code deve ser 200.
        O corpo da resposta deve conter o mesmo id enviado (1).
        O corpo da resposta deve conter a mesma url enviada.

02. Atualização de Recurso (PUT)
Identificador: TC-UPDATE-002 Descrição: Validar a atualização da URL de uma capa existente.
    Endpoint: PUT /CoverPhotos/1
    Payload de Envio (JSON):

    {
        "id": 1,
        "idBook": 1,
        "url": "https://example.com/updated_cover_photo.jpg"
    }

    Procedimento:
        Enviar a requisição PUT apontando para o ID 1.
        Verificar se o JSON retornado reflete as mudanças.

    Critérios de Aceite:
        Status Code deve ser 200.
        A propriedade url na resposta deve ser "https://example.com/updated_cover_photo.jpg".
        Os IDs (id e idBook) devem permanecer inalterados.

03. Listagem de Recursos (GET All)
Identificador: TC-LIST-003 Descrição: Garantir que a API retorne a coleção completa de capas de livros.
    Endpoint: GET /CoverPhotos
    Payload: (Vazio)
    Procedimento:
        Realizar a chamada GET na raiz do recurso.

    Critérios de Aceite:
        Status Code deve ser 200.
        O retorno deve ser do tipo Array (Lista).
        A contagem de itens na lista deve ser maior que 0 (len(data) > 0).

04. Consulta Específica (GET ID)

Identificador: TC-READ-004 Descrição: Validar a recuperação de uma única capa baseada em seu ID.
    Endpoint: GET /CoverPhotos/1
    Payload: (Vazio)
    Procedimento:
        Realizar a chamada GET passando o ID 1 na URL.

    Critérios de Aceite:
        Status Code deve ser 200.
        O objeto JSON retornado deve possuir a chave "id": 1.

05. Remoção de Recurso (DELETE)
Identificador: TC-DELETE-005 Descrição: Verificar se a requisição de exclusão é processada corretamente.
    Endpoint: DELETE /CoverPhotos/1
    Payload: (Vazio)
    Procedimento:
        Enviar o comando DELETE para o ID especificado.

    Critérios de Aceite:
        Status Code deve ser 200.
