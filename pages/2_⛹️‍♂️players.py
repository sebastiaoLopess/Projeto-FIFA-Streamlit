import streamlit as st

df_data = st.session_state["data"] # carregando o estado do dataset da outra pagina

clubes = df_data["Club"].unique() # carregando os valores unicos da coluna club
club = st.sidebar.selectbox("Clube", clubes) # incluindo um filtro selectbox dentro do sidebar pegando so o resultado de clubes

# fazendo o mesmo processo so que para jogadores
df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)