import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title = "Home",
    page_icon= "src/imgs/logo ventures.png",
    layout='wide'
)

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


#Validade por ano e mês

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

def filter(optionMes, optionLote, optionAno):

    if optionLote == "Lote 1":

        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]
        
        if optionAno and mes_opcao:
            dfLote1['Ano'] = dfLote1['Validade'].str.split('/').str[2]
            dfLote1['Mes'] = dfLote1['Validade'].str.split('/').str[1]
            dfMesLote1 = dfLote1[(dfLote1['Ano'] == optionAno) & (dfLote1['Mes'] == mes_opcao)]
            dfMesLote1 = dfMesLote1.drop(columns=['Ano', 'Mes'])

        st.table(dfMesLote1)

    elif optionLote == "Lote 2":
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]

        if optionAno and mes_opcao:
            dfLote2['Ano'] = dfLote2['Validade2'].str.split('/').str[2]
            dfLote2['Mes'] = dfLote2['Validade2'].str.split('/').str[1]
            dfMesLote2 = dfLote2[(dfLote2['Ano'] == optionAno) & (dfLote2['Mes'] == mes_opcao)]
            dfMesLote2 = dfMesLote2.drop(columns=['Ano', 'Mes'])


        st.table(dfMesLote2)        
        

    elif optionLote == "Lote 3":
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }
        # Extrair o número do mês do option
        mes_opcao = meses_dict[optionMes]

        if optionAno and mes_opcao:
            dfLote3['Ano'] = dfLote3['Validade3'].str.split('/').str[2]
            dfLote3['Mes'] = dfLote3['Validade3'].str.split('/').str[1]
            dfMesLote3 = dfLote3[(dfLote3['Ano'] == optionAno) & (dfLote3['Mes'] == mes_opcao)]
            dfMesLote3 = dfMesLote3.drop(columns=['Ano', 'Mes'])

        st.table(dfMesLote3)
    else:
        meses_dict = {
            "JAN": "01", "FEV": "02", "MAR": "03", "ABR": "04",
            "MAI": "05", "JUN": "06", "JUL": "07", "AGO": "08",
            "SET": "09", "OUT": "10", "NOV": "11", "DEZ": "12"
        }

        mes_opcao = meses_dict[optionMes]

        
        if optionAno and mes_opcao:
            dfLote4['Ano'] = dfLote4['Validade4'].str.split('/').str[2]
            dfLote4['Mes'] = dfLote4['Validade4'].str.split('/').str[1]
            dfMesLote4 = dfLote4[(dfLote4['Ano'] == optionAno) & (dfLote4['Mes'] == mes_opcao)]
            dfMesLote4 = dfMesLote4.drop(columns=['Ano', 'Mes'])

        st.table(dfMesLote4)

st.markdown(""" <h3> Filtro de validade por ano e mês </h3>""", unsafe_allow_html=True)

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

st.divider()



#NOVO GRÁFICO
col1, col2 = col1, col2 = st.columns([0.6, 0.3], gap="large")

with col1:

    colunasBar = ["Custo Unit.", "Código"]
    dfCustoUnit = pd.read_csv("data/preco_custo.csv", usecols=colunasBar)

    # Remover o símbolo R$ e espaços
    dfCustoUnit['Custo Unit.'] = dfCustoUnit['Custo Unit.'].str.replace('R$', '').str.strip()

    # Substituir a vírgula por ponto e converter para float, depois para int
    dfCustoUnit['Custo Unit.'] = dfCustoUnit['Custo Unit.'].str.replace('.', '').str.replace(',', '.').astype(float).astype(int)

    dfCustoUnit = dfCustoUnit.iloc[:-1]

    # Configurar o título do dashboard
    st.markdown(""" <h3> Custos Unitários dos insumos </h3>""", unsafe_allow_html=True)

    threshold = st.slider("Definir limite de custo unitário", min_value=0, max_value=8000, value=0)

    # Filtrar produtos com custos unitários altos
    dfHighCost = dfCustoUnit[dfCustoUnit['Custo Unit.'] > threshold]

    st.bar_chart(
    dfHighCost, x="Código", y=["Custo Unit.", "Custo Unit."], color=["#8602f3", "#8602f3"]  # Optional
    )

with col2:

    colunasBar3 = ["Custo Unit.", "Código"]
    dfCustoUnit3 = pd.read_csv("data/preco_custo.csv", usecols=colunasBar3)
    # Remover o símbolo R$ e espaços
    dfCustoUnit3['Custo Unit.'] = dfCustoUnit3['Custo Unit.'].str.replace('R$', '').str.strip()

    # Substituir a vírgula por ponto e converter para float, depois para int
    dfCustoUnit3['Custo Unit.'] = dfCustoUnit3['Custo Unit.'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float).astype(int)

    # Apagar a última linha do DataFrame (se necessário)
    dfCustoUnit3 = dfCustoUnit3.iloc[:-1]

    # Ordenar os dados pelo custo unitário em ordem decrescente
    dfCustoUnit3 = dfCustoUnit3.sort_values(by='Custo Unit.', ascending=False)

    # Selecionar os 3 insumos com maiores custos
    dfTop3 = dfCustoUnit.head(3)

    # Configurar o título do dashboard

    st.markdown(""" <h4 class="titulo_custos"> Top 3 insumos com maiores custos unitários </h4>""", unsafe_allow_html=True)
    st.bar_chart(
    dfTop3, x="Código", y=["Custo Unit.", "Custo Unit." ], color=["#8602f3", "#8602f3"] 
    )
 