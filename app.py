import streamlit as st
import pandas as pd
import pyodbc

def criar_conexao():
    servidor = 'ANA'
    banco = 'Locadora_1'

    config_conn = ("Driver={ODBC Driver 17 for SQL Server};"
               f"Server={servidor};"
               f"Database={banco};"
               "Trusted_Connection=yes;")
    return pyodbc.connect(config_conn)

st.set_page_config(page_title="Dashboard Ana", layout="wide")
st.title("Explorador de dados: Locadora")

lista_tabelas = [
    ' dbo.Tbl_Clientes',
    'dbo.Tbl_DetalhesDoPedido',
    'dbo.Tbl_Filmes',
    'dbo.Tbl_Genero',
    'dbo.Tbl_Pedidos'
]
tabela_selecionada = st.sidebar.selectbox("Selecione a Tabela para Visualizar:", lista_tabelas)

try:
    conn = criar_conexao()
    query = f"SELECT * FROM {tabela_selecionada}"
    df = pd.read_sql(query, conn)
    col1, col2 = st.columns(2)
    col1.metric("Total de Registros", len(df))
    col2.metric("Total de Colunas", len(df.columns))

    st.subheader(f"Dados da tabela:{tabela_selecionada}")
    st.dataframe(df, use_container_width=True)

except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")

