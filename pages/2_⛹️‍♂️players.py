import streamlit as st

st.set_page_config(
    page_title="Players",
    layout="wide"
)

df_data = st.session_state["data"] # carregando o estado do dataset da outra pagina

clubes = df_data["Club"].unique() # carregando os valores unicos da coluna club
club = st.sidebar.selectbox("Clube", clubes) # incluindo um filtro selectbox dentro do sidebar pegando so o resultado de clubes

# fazendo o mesmo processo so que para jogadores
df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1,col2,col3,col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")