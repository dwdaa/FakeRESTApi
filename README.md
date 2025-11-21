## 📄 README.md: Casos de Teste CRUD em Ambiente Swagger (FakeRESTApi) 

### 1. Visão Geral

Este projeto foi desenvolvido para atender aos requisitos acadêmicos de Engenharia de Software, focando na validação de uma API através da implementação de **cinco casos de teste CRUD** (Create, Read, Update, Delete) individuais.

* **API Alvo:** FakeRESTApi (Documentação Swagger/OpenAPI)
* **URL Base:** `https://fakerestapi.azurewebsites.net/api/v1`
* **Recurso Testado:** /Activities, /Authors /Books,/Users e /CoverPhotos
* **Metodologia:** Behavior-Driven Development (BDD) / Testes de Integração com Pytest
* **Requisito de Escopo:** O projeto como um todo simula uma API com **30 *endpoints***, abrangendo múltiplos recursos, conforme a lista de especificação do trabalho.

***

### 2. Configuração do Ambiente

Para executar os testes, é necessário ter o Python 3 instalado e configurar um ambiente virtual (VENV).

#### 2.1. Criar e Ativar o VENV

1.  Navegue até a pasta raiz do projeto.
2.  Crie o ambiente virtual:
    ```bash
    python3 -m venv venv
    ```
3.  Ative o ambiente (Exemplo para Windows PowerShell):
    ```bash
    .\venv\Scripts\Activate.ps1
    ```

#### 2.2. Instalar Dependências

Com o VENV ativado, instale as bibliotecas necessárias:

```bash
pip install pytest requests
```

### 3. Estrutura do Projeto
O projeto segue a estrutura padrão de testes Python e a organização por aluno/método:

/Projeto_Testes_API
├── venv/                     # Ambiente Virtual
├── README.md                 # Este arquivo
└── tests/
    └──[nome_do_aluno]/ 
        ├──TCs-aluno.feature   
        ├── test_post.py      # Casos de Teste: POST (Create)
        ├── test_get.py       # Casos de Teste: GET (Read)
        ├── test_put.py       # Casos de Teste: PUT (Update)
        └── test_delete.py    # Casos de Teste: DELETE (Delete)

### 4. Execução do testes

Para executar os testes use o comando:

```bash
pytest
```

Use as flags -v (verbose) e -s (capturar output) para verificar o Status Code de cada requisição e o resultado detalhado dos testes:

```bash
pytest -vs
```
