# Mini Projeto 3 - API de Técnicas de Judô

O projeto foi desenvolvido em dupla (Debora Rubio e Paulo Fonseca), seguindo as boas práticas de versionamento no GitHub. O histórico do repositório reflete as contribuições mútuas, incluindo o fluxo de desenvolvimento colaborativo e submissões registradas, para a disciplina de Linguagem de Programação II do curso de Inteligência Artificial da Fatec Centro Paula Souza. O projeto consiste na implementação de uma arquitetura Cliente/Servidor para listar e consumir dados estruturados (JSON) sobre golpes de Judô.


## Tecnologias Utilizadas

* **Python 3.11+**
* **FastAPI**: Framework de alta performance para a criação da API (Backend).
* **Uvicorn**: Servidor ASGI para executar a aplicação web.
* **Requests**: Biblioteca HTTP para consumo de dados pelo lado do cliente.


## Estrutura do Projeto

```text
MINI_PROJETO_3-API/
├── client/
│   └── main.py          # Script cliente que consome a API e exibe os golpes
├── servidor/
│   └── servidor.py      # Script do servidor que disponibiliza os dados em JSON
├── venv/                # Ambiente virtual Python
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências globais do projeto



Como Executar o Projeto
Para rodar o projeto localmente, certifique-se de que os comandos sejam executados a partir das pastas corretas no terminal do VS Code.

1. Inicializando o Servidor (Backend)
Abra o terminal integrado diretamente na pasta servidor/.

Ative o ambiente virtual executando:

..\venv\Scripts\Activate.ps1

Inicie o servidor FastAPI com o Uvicorn:

py -m uvicorn servidor:tecnicas --reload

O servidor estará rodando no endereço local: http://127.0.0.1:8000/

2. Executando o Cliente (Frontend Terminal)
Abra um segundo terminal integrado, desta vez na pasta client/.

Ative o ambiente virtual executando:

..\venv\Scripts\Activate.ps1

Execute o script para consumir os dados do servidor:

py main.py

