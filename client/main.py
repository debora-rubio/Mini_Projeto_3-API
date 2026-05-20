
# Para rodar o código cliente, use o comando: streamlit run main.py

import streamlit as st
import requests


st.title("Catálogo de Golpes de Judô")
st.write("Dados puxados direto da API FastAPI")

# Endereço do seu servidor
URL_DA_API = "http://127.0.0.1:8000/"

# Faz o pedido dos dados para o servidor
resposta = requests.get(URL_DA_API)

# Se a comunicação funcionou (Código 200)
if resposta.status_code == 200:
    lista_de_golpes = resposta.json()
    
    # Passa por cada golpe da lista (igualzinho ao código de terminal)
    for golpe in lista_de_golpes:
        st.header(f"Nome: {golpe['nome']}")
        st.write(f"**Categoria:** {golpe['categoria']}")
        st.write(f"**Descrição:** {golpe['descricao']}")
        
        # Mostra a imagem do golpe na tela usando o link do servidor
        st.image(golpe['imagem'])
        
        st.write("---") # Linha separadora entre um golpe e outro
else:
    st.error("Erro ao se conectar com o servidor.")