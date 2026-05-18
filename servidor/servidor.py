# Quando for preciso rodar o programa --> py -m uvicorn servidor:tecnicas --reload

# No terminal:
#   • py -m pip install fastapi
#       ♦ fastapi --> Biblioteca usada para criar uma API (Interface de Programação de Aplicações)
#       ♦ Define rotas e respostas
#   • py -m pip install uvicorn --> Servidor que executa a API e mostra no navegador

from fastapi import FastAPI # Classe da biblioteca fastapi que cria a nossa aplicação

tecnicas = FastAPI() 

# A LINHA DO .mount() FOI REMOVIDA DAQUI PORQUE NÃO USAMOS MAIS IMAGENS FÍSICAS!

@tecnicas.get("/")
def home():
    dados_dos_golpes = [
        {"id": 1, "nome": "Seoi Nage 001", "categoria": "Te-waza (Braço)", "descricao": "Técnica de arremesso sobre o ombro.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Seoi Nage 001.jpg"},
        {"id": 2, "nome": "Obi Tori Gaeshi 002", "categoria": "Te-waza (Braço)", "descricao": "Arremesso segurando a faixa.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Obi Tori Gaeshi 002.jpg"},
        {"id": 3, "nome": "Sode Tsuri Komi Goshi 003", "categoria": "Koshi-waza (Quadril)", "descricao": "Arremesso pelo quadril levantando a manga.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Sode Tsuri Komi Goshi 003.jpg"},
        {"id": 4, "nome": "O Uchi Gari 004", "categoria": "Ashi-waza (Perna)", "descricao": "Grande ganchada interna por dentro.", "imagem": "http://127.0.0.1:8000/qualquer_nome/O Uchi Gari 004.jpg"},
        {"id": 5, "nome": "O Soto Otoshi 005", "categoria": "Ashi-waza (Perna)", "descricao": "Grande queda por fora derrubando a perna.", "imagem": "http://127.0.0.1:8000/qualquer_nome/O Soto Otoshi 005.jpg"},
        {"id": 6, "nome": "Ippon Seoi Nage 006", "categoria": "Te-waza (Braço)", "descricao": "Arremesso por um único braço sobre o ombro.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Ippon Seoi Nage 006.jpg"},
        {"id": 7, "nome": "Morote Gari 007", "categoria": "Te-waza (Braço)", "descricao": "Segurada com as duas mãos nas pernas (catada de perna).", "imagem": "http://127.0.0.1:8000/qualquer_nome/Morote Gari 007.jpg"},
        {"id": 8, "nome": "Harai Goshi 008", "categoria": "Koshi-waza (Quadril)", "descricao": "Arremesso varrendo com o quadril.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Harai Goshi 008.jpg"},
        {"id": 9, "nome": "Ko Soto Gari 009", "categoria": "Ashi-waza (Perna)", "descricao": "Pequena ganchada externa por fora.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Ko Soto Gari 009.jpg"},
        {"id": 10, "nome": "Tsubame Gaeshi 010", "categoria": "Ashi-waza (Perna)", "descricao": "Contra-golpe da andorinha.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Tsubame Gaeshi 010.jpg"},
        {"id": 11, "nome": "Seoi Otoshi 011", "categoria": "Te-waza (Braço)", "descricao": "Queda sobre o ombro derrubando de joelhos.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Seoi Otoshi 011.jpg"},
        {"id": 12, "nome": "Kuchiki Taoshi 012", "categoria": "Te-waza (Braço)", "descricao": "Derrubada puxando a perna com uma das mãos.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Kuchiki Taoshi 012.jpg"},
        {"id": 13, "nome": "(Ko-) (O-) Tsuri Goshi 013", "categoria": "Koshi-waza (Quadril)", "descricao": "Técnica de puxada pelo quadril.", "imagem": "http://127.0.0.1:8000/qualquer_nome/(Ko-) (O-) Tsuri Goshi 013.jpg"},
        {"id": 14, "nome": "Ko Uchi Gari 014", "categoria": "Ashi-waza (Perna)", "descricao": "Pequena ganchada interna por dentro.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Ko Uchi Gari 014.jpg"},
        {"id": 15, "nome": "O Soto Gaeshi 015", "categoria": "Ashi-waza (Perna)", "descricao": "Contra-golpe de grande ganchada externa.", "imagem": "http://127.0.0.1:8000/qualquer_nome/O Soto Gaeshi 015.jpg"},
        {"id": 16, "nome": "Tai Otoshi 016", "categoria": "Te-waza (Braço)", "descricao": "Queda do corpo usando a perna como barreira.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Tai Otoshi 016.jpg"},
        {"id": 17, "nome": "Kibisu Gaeshi 017", "categoria": "Te-waza (Braço)", "descricao": "Queda segurando o calcanhar.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Kibisu Gaeshi 017.jpg"},
        {"id": 18, "nome": "Hane Goshi 018", "categoria": "Koshi-waza (Quadril)", "descricao": "Arremesso com o quadril em mola.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Hane Goshi 018.jpg"},
        {"id": 19, "nome": "Okuri Ashi Harai 019", "categoria": "Ashi-waza (Perna)", "descricao": "Varrida de ambas as pernas em deslocamento lateral.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Okuri Ashi Harai 019.jpg"},
        {"id": 20, "nome": "O Uchi Gaeshi 020", "categoria": "Ashi-waza (Perna)", "descricao": "Contra-golpe de grande ganchada interna.", "imagem": "http://127.0.0.1:8000/qualquer_nome/O Uchi Gaeshi 020.jpg"},
        {"id": 21, "nome": "Kata Guruma 021", "categoria": "Te-waza (Braço)", "descricao": "Roda de ombro (carregar nos ombros).", "imagem": "http://127.0.0.1:8000/qualquer_nome/Kata Guruma 021.jpg"},
        {"id": 22, "nome": "Uchi Mata Sukashi 022", "categoria": "Ashi-waza (Perna)", "descricao": "Esquiva e contra-golpe da técnica Uchi Mata.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Uchi Mata Sukashi 022.jpg"},
        {"id": 23, "nome": "Utsuri Goshi 023", "categoria": "Koshi-waza (Quadril)", "descricao": "Mudança ou transferência de quadril.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Utsuri Goshi 023.jpg"},
        {"id": 24, "nome": "Uchi Mata 024", "categoria": "Ashi-waza (Perna)", "descricao": "Arremesso aplicando a coxa na parte interna das pernas.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Uchi Mata 024.jpg"},
        {"id": 25, "nome": "Hane Goshi Gaeshi 025", "categoria": "Koshi-waza (Quadril)", "descricao": "Contra-golpe de Hane Goshi.", "imagem": "http://127.0.0.1:8000/qualquer_nome/Hane Goshi Gaeshi 025.jpg"}
    ]
    return dados_dos_golpes