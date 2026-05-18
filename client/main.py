import requests

# 1. Definimos o endereço (URL) onde o servidor atualizado do Paulo está rodando
# Como ele colocou os dados JSON direto na rota principal, usamos a barra "/"
URL_DA_API = "http://127.0.0.1:8000/"

def buscar_e_mostrar_golpes():
    print("=== ACESSANDO O CATÁLOGO DE GOLPES DE JUDÔ ===")
    
    try:
        # 2. Faz o pedido dos dados JSON para o servidor
        resposta = requests.get(URL_DA_API)
        
        # 3. Se o código for 200, a comunicação funcionou perfeitamente!
        if resposta.status_code == 200:
            
            # 4. Transformamos o JSON recebido na lista oficial de golpes do Python
            lista_de_golpes = resposta.json()
            
            print(f"Sucesso! Foram encontrados {len(lista_de_golpes)} golpes no servidor.\n")
            
            # 5. Loop para passar por cada um dos 25 golpes e exibir no terminal
            for golpe in lista_de_golpes:
                print(f"ID: {golpe['id']}")
                print(f"Nome do Golpe: {golpe['nome']}")
                print(f"Categoria: {golpe['categoria']}")
                print(f"Descrição: {golpe['descricao']}")
                print(f"Link da Imagem: {golpe['imagem']}")
                print("-" * 40) # Linha separadora
                
        else:
            print(f"Erro no servidor: Código {resposta.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível se conectar ao servidor.")
        print("Certifique-se de que o servidor do FastAPI está ligado e rodando na rota correta!")

if __name__ == "__main__":
    buscar_e_mostrar_golpes()