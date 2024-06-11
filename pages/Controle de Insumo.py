#a) Índices de perdas e/ou rendimento dos lotes.
#b) Custo (R$) das perdas.
#g) Controle da validade dos insumos.
#h) Sinalização dos insumos mais próximos do vencimento.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

from subpages.gh_mes import callmes
from subpages.gh_codigo import callcodigo

st.set_page_config(
    page_title = "Home",
    page_icon= "src/imgs/logo ventures.png",
    layout='wide'
)


# ------------------------------------ HEADER -----------------------------------
st.markdown("<h1 style='text-align: center; color: #fff;'>Controle de Insumos</h1>", unsafe_allow_html=True)


# ---------------------------------- FIM HEADER -----------------------------------


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ SIDEBAR ///////////////////////////////////
menu = ['Global', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ',]
choice = st.sidebar.selectbox("Selecione o mês que deseja visualizar:", menu)

query = st.sidebar.text_input(
        "Entre com o Código do Insumo especifico:",
        placeholder="This is a placeholder",
    )
if query:
    
    callcodigo(query)



#if query:
#    mask = dfGlobal.applymap(lambda x: query in str(x).lower()).any(axis=1)
#    df = dfGlobal[mask]

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ FIM SIDEBAR //////////////////////////////// 

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx BODY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
# Excluir as colunas
def main():
    if choice == 'Global':
        st.write('## Global')
        dfGlobal = pd.read_csv("D:/Programação/VSCode/praticando/pythonCRUD/crudpython/LAFEPE-ProjetAI/data/copiainsumo.csv")
        dfGlobal['Código MP'] = dfGlobal['Código MP'].astype(str)
        st.dataframe(dfGlobal, height=700, width=2000, use_container_width=False)
        #print(dfTest)
        #st.dataframe(dfTest)
        #print(dfGlobal['Código MP'])

    if choice == 'JAN':
        st.write('## Janeiro')
        #st.line_chart(st.dataframe(df_Jan))
        callmes("JAN")

    if choice == 'FEV':
        st.write('## Fevereiro')
        callmes('FEV')

    if choice == 'MAR':
        st.write('## Março')
        callmes('MAR')
    
    if choice == 'ABR':
        st.write('## Abril')
        callmes('ABR')
    
    if choice == 'MAI':
        st.write('## Maio')
        callmes('MAI')

    if choice == 'JUN':
        st.write('## Junho')
        callmes('JUN')
    
    if choice == 'JUL':
        st.write('## Julho')
        callmes('JUL')

    if choice == 'AGO':
        st.write('## Agosto')
        callmes('AGO')

    if choice == 'SET':
        st.write('## Setembro')
        callmes('SET')

    if choice == 'OUT':
        st.write('## Outubro')
        callmes('OUT')

    if choice == 'NOV':
        st.write('## Novembro')
        callmes('NOV')

    if choice == 'DEZ':
        st.write('## Dezembro')
        callmes('DEZ')

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx FIM BODY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 



if __name__ == '__main__':
    main()