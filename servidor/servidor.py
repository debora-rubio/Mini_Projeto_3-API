# Quando for preciso rodar o programa --> py -m uvicorn servidor:tecnicas --reload

# No terminal:
#   • py -m pip install fastapi
#       ♦ fastapi --> Biblioteca usada para criar uma API (Interface de Programação de Aplicações)
#       ♦ Define rotas e respostas
#   • py -m pip install uvicorn --> Servidor que executa a API e mostra no navegador

from fastapi import FastAPI # FastAPI --> Classe da biblioteca fastapi que cria uma aplicação web (ou seja, um servidor)
from fastapi.staticfiles import StaticFiles
#   • staticfiles --> Submódulo que cuida de arquivos estáticos (.jpg, .mp4 etc.)
#   • StaticFiles --> Ferramenta que libera uma pasta para o navegador acessar
from fastapi.responses import HTMLResponse # --> Serve para enviar uma HTML para o navegador

tecnicas = FastAPI() # FastAPI --> Classe da biblioteca fastapi que cria uma aplicação web (ou seja, um servidor)

tecnicas.mount("/qualquer_nome", StaticFiles(directory="imagens"), name="nome_desta_configuração")
# tecnicas --> A aplicação FastAPI (ou seja, o servidor)

# .mount() --> Significa “conectar” e anexa uma pasta/arquivo ao servidor

# "/qualquer_nome" --> Caminho (URL) no navegador para acessar os arquivos da pasta

# StaticFiles() --> Ferramenta que serve (entrega) arquivos estáticos (.jpg, .mp4 etc.)

# directory="imagens" --> Indica qual pasta do computador será servida

# name="nome_desta_configuração" --> É exatamente isto: o nome dado à configuração

@tecnicas.get("/", response_class=HTMLResponse)
def home():

    html = """
    <html>
        <head>
            <title>Algumas técnicas</title>
        </head>

        <body>
            <h1> T É C N I C A S </h1>

            <h2> NOME DA IMAGEM_001 </h2>
            <p> GRUPO: TIPO 1 </p>
            <img src="/qualquer_nome/teste1.jpg" width="300">

            <hr>

            <h2> NOME DA IMAGEM_002 </h2>
            <p> GRUPO: TIPO 2 </p>
            <img src="/qualquer_nome/teste2.jpg" width="300">

        </body>
    </html>
    """

    return html

# teste 001