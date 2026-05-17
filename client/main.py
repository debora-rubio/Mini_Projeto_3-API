import requests

# 1. Definimos o endereço (URL) onde o servidor do seu parceiro vai rodar
# O FastAPI por padrão roda no endereço http://127.0.0.1:8000
# E a rota que vai listar os golpes será a '/golpes'
URL_DA_API = "http://127.0.0.1:8000/golpes"

def buscar_e_mostrar_golpes():
    print("=== ACESSANDO O CATÁLOGO DE GOLPES DE JUDÔ ===")
    
    try:
        # 2. O 'requests.get' faz o pedido ("me dá os dados") para o servidor
        resposta = requests.get(URL_DA_API)
        
        # 3. Se a resposta vier com o código HTTP 200, significa que deu certo!
        if resposta.status_code == 200:
            
            # 4. Transformamos o JSON que veio do servidor em uma lista do Python
            lista_de_golpes = resposta.json()
            
            print(f"Sucesso! Foram encontrados {len(lista_de_golpes)} golpes.\n")
            
            # 5. Fazemos um loop (for) para passar de golpe em golpe e mostrar na tela
            for golpe in lista_de_golpes:
                print(f"ID: {golpe['id']}")
                print(f"Nome do Golpe: {golpe['nome']}")
                print(f"Categoria: {golpe['categoria']}")
                print(f"Descrição: {golpe['descricao']}")
                print(f"Arquivo da Imagem: {golpe['imagem']}")
                print("-" * 40) # Apenas uma linha para separar um golpe do outro
                
        else:
            print(f"Erro no servidor: Código {resposta.status_code}")
            
    except requests.exceptions.ConnectionError:
        # Esse erro acontece se você tentar rodar o cliente sem o servidor estar ligado
        print("Erro: Não foi possível se conectar ao servidor.")
        print("Certifique-se de que o servidor do FastAPI está ligado e rodando!")

# Este bloco diz para o Python executar a nossa função assim que o arquivo for rodado
if __name__ == "__main__":
    buscar_e_mostrar_golpes()