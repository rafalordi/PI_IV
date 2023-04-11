import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

file = 'Banco de Dados/Teste.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(file, encoding='latin-1', sep = ';')

    return df
df = load_data()

image = Image.open('Fotos/univesp.png')

with st.columns(3)[1]:
    st.image(image, use_column_width='auto')

st.title("Honest Fuel – Análises de Preços de Combustíveis")
st.markdown(
    """
    :bar_chart: Dashboard
    """""
)

st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar tabela"):
        st.markdown("### Tabela de dados")
        st.write(df)

# ---- SIDEBAR ----
customer_type = st.sidebar.multiselect(
    "Selecione o combustivel:",
    options=df["Produto"].unique(),
    #default=df["Produto"].unique(),
)

gender = st.sidebar.multiselect(
    "Selecione a unidade de medida:",
    options=df["Unidade_de_Medida"].unique(),
    #default=df["Unidade_de_Medida"].unique()
)

city = st.sidebar.multiselect(
  "Selecio o municipio:",
   options=df["Municipio"].unique(),
   #default=df["Municipio"].unique()
)

df_selection = df.query(
    "Municipio == @city & Produto ==@customer_type & Unidade_de_Medida == @gender"
)

chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['Gasolina', 'Etanol', 'Diesel', 'GNV'])

st.bar_chart(df, y='Produto', x='Valor_de_Venda')

st.line_chart(chart_data)

st.bar_chart(chart_data)


