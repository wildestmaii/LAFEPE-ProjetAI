import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Home",
    page_icon= "src/imgs/logo ventures.png",
    layout='wide'
)

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

colunas = ["Código MP", "Lote 01", "Validade", "Lote 02", "Validade2", "Lote 03", "Validade3", "Lote 04", "Validade4"]
df = pd.read_csv("data/validade.csv", usecols=colunas)
df = df.astype(str)

colunasLote1 = ["Código MP", "Lote 01", "Validade"]
dfLote1 = pd.read_csv("data/validade.csv", usecols=colunasLote1)
dfLote1 = dfLote1.astype(str)


colunasLote2 = ["Código MP", "Lote 02", "Validade2"]
dfLote2 = pd.read_csv("data/validade.csv", usecols=colunasLote2)
dfLote2 = dfLote2.astype(str)

colunasLote3 = ["Código MP", "Lote 03", "Validade3"]
dfLote3 = pd.read_csv("data/validade.csv", usecols=colunasLote3)
dfLote3 = dfLote3.astype(str)

colunasLote4 = ["Código MP", "Lote 04", "Validade4"]
dfLote4 = pd.read_csv("data/validade.csv", usecols=colunasLote4)
dfLote4 = dfLote4.astype(str)

def filter(optionMes, optionAno, optionLote):

    if optionLote == "Lote 1":

        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]
        print("porra")
        
        # Filtrar o DataFrame para mostrar apenas as linhas onde o ano é igual ao ano selecionado
        dfMesLote1 = dfLote1[dfLote1['Validade'].str.split('/').str[1] == mes_opcao]
        st.write("Lote 1 (Filtrado por Ano):")
        st.table(dfMesLote1)

    elif optionLote == "Lote 2":
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]

        # Filtrar o DataFrame para mostrar apenas as linhas onde o mês é igual ao mês selecionado na coluna "Validade"
        dfMesLote2 = dfLote2[dfLote2['Validade2'].str.split('/').str[1] == mes_opcao]
        
        # Exibir o DataFrame filtrado
        st.write("Lote 2:")
        st.table(dfMesLote2)

    elif optionLote == "Lote 3":
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }
        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]

        # Filtrar o DataFrame para mostrar apenas as linhas onde o mês é igual ao mês selecionado na coluna "Validade"
        dfMesLote3 = dfLote3[dfLote3['Validade3'].str.split('/').str[1] == mes_opcao]
        
        # Exibir o DataFrame filtrado
        st.write("Lote 3:")
        st.table(dfMesLote3)
    else:
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        mes_opcao = meses_dict[optionMes]

        # Filtrar o DataFrame para mostrar apenas as linhas onde o mês é igual ao mês selecionado na coluna "Validade"
        dfMesLote4 = dfLote4[dfLote4['Validade4'].str.split('/').str[1] == mes_opcao]
        
        st.write("Lote 4:")
        st.table(dfMesLote4)

st.markdown(""" <h4> Filtro de validade por ano e mês </h4>""", unsafe_allow_html=True)

col1, col2 = st.columns([0.3, 0.6])
with col1: 
   
    optionLote = st.selectbox(
        "Selecione o Lote:",
        ("Lote 1", "Lote 2", "Lote 3", "Lote 4"))

    optionMes = st.selectbox(
        "Selecione Mês:",
        ("JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"), index=0)


    # Concatenar as colunas de validade em uma única série e extrair os anos
    anos_validade = pd.concat([df['Validade'], df['Validade2'], df['Validade3'], df['Validade4']]).str.extract(r'(\d{4})', expand=False)

    # Remover valores duplicados, None e NaN
    anos_validade = anos_validade.dropna().unique()


    optionAno = st.selectbox(
        "Selecione o ano:",
        anos_validade
    )

    

with col2:
    st.markdown(""" <h5>Tabela Filtrada</h5>""", unsafe_allow_html=True)
    filter(optionMes, optionLote, optionAno)
    print("alo")

st.divider()