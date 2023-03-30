import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'Banco de Dados/Combustiveis.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(file, encoding='latin-1', sep = ';')


    return df
df = load_data()
st.title("Preço dos combustiveis 2023")
st.markdown(
    """
    Dashboard
    """""
)

st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar tabela"):
        st.markdown("### Tabela de dados")
        st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

