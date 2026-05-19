import requests

# 1. Definimos o endereço (URL) onde o servidor FastAPI está rodando.
# Ele fará a requisição na rota principal "/" para obter o JSON dos 25 golpes.
# Para rodar o cliente, use o comando: py main.py

URL_DA_API = "http://127.0.0.1:8000/"

def buscar_e_mostrar_golpes():
    print("==================================================")
    print("=== ACESSANDO O CATÁLOGO DE GOLPES DE JUDÔ ===")
    print("==================================================\n")
    
    try:
        # 2. Faz o pedido (requisição GET) dos dados para o servidor
        resposta = requests.get(URL_DA_API)
        
        # 3. Se o código for 200, a comunicação com o servidor foi um sucesso!
        if resposta.status_code == 200:
            
            # 4. Convertemos o JSON recebido na lista oficial de golpes do Python
            lista_de_golpes = resposta.json()
            
            print(f" Sucesso! Foram encontrados {len(lista_de_golpes)} golpes no servidor.\n")
            print("-" * 50)
            
            # 5. Passamos por cada um dos golpes para exibir as informações e os links das fotos
            for golpe in lista_de_golpes:
                print(f" ID: {golpe['id']}")
                print(f" Nome do Golpe: {golpe['nome']}")
                print(f" Categoria: {golpe['categoria']}")
                print(f" Descrição: {golpe['descricao']}")
                # Aqui o cliente lê com sucesso a URL com o caminho '/imagens/' atualizado do servidor
                print(f" URL da Imagem: {golpe['imagem']}")
                print("-" * 50) # Linha separadora entre os golpes
                
        else:
            print(f" Erro no servidor: Código de status {resposta.status_code}")
            
    except requests.exceptions.ConnectionError:
        print(" Erro: Não foi possível se conectar ao servidor.")
        print(" Certifique-se de que o servidor do FastAPI está ligado no outro terminal antes de rodar o cliente!")

if __name__ == "__main__":
    buscar_e_mostrar_golpes()