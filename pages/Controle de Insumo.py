#a) Índices de perdas e/ou rendimento dos lotes.
#b) Custo (R$) das perdas.
#g) Controle da validade dos insumos.
#h) Sinalização dos insumos mais próximos do vencimento.

# ********************************* LIBRARIES & CONFIG *********************************
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.figure_factory as ff

from subpages.gh_mes import callmes
from subpages.gh_codigo import callcodigo

st.set_page_config(
    page_title = "Home",
    page_icon= "src/imgs/logo ventures.png",
    layout='wide'
)
# ******************************** FIM LIBRARIES & CONFIG ******************************

with open('src/style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



# ------------------------------------ HEADER -----------------------------------
st.markdown("<h1 style='text-align: center'>Controle de Insumos</h1>", unsafe_allow_html=True)

url = "https://raw.githubusercontent.com/wildestmaii/LAFEPE-ProjetAI/raralaraloralisa/data/copiainsumo.csv?token=GHSAT0AAAAAACSP5N722DI3D3KYEQI2PYTQZTJBM4A"

clearScreen = st.empty()

# ---------------------------------- FIM HEADER -----------------------------------




# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ SIDEBAR ///////////////////////////////////
menu = ['Global', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'FEV05', 'MAR05']
choice = st.sidebar.selectbox("Selecione o mês que deseja visualizar:", menu)

query = st.sidebar.text_input(
        "Entre com o Código do Insumo especifico:",
        placeholder="This is a placeholder",
    )

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ FIM SIDEBAR //////////////////////////////// 




# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx BODY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
# Fucntion Main

def main():
    if query:
        clearScreen.write('query')
        callcodigo(query, url, clearScreen)
    
    else:
        #Switch Case - Filter Choice
        if choice == 'Global':
            #dfGlobal = pd.read_csv("D:/Programação/VSCode/praticando/pythonCRUD/crudpython/LAFEPE-ProjetAI/data/copiainsumo.csv")
            dfGlobal = pd.read_csv(url)
            dfGlobal['Código MP'] = dfGlobal['Código MP'].astype(str)
            clearScreen.write('### Dados Gerais')
            st.dataframe(dfGlobal, height=700, width=2000, use_container_width=False)

        if choice == 'JAN':
            st.write('## Janeiro')
            #st.line_chart(st.dataframe(df_Jan))
            callmes("JAN04", url, clearScreen)

        if choice == 'FEV':
            st.write('## Fevereiro')
            callmes('FEV', url, clearScreen)

        if choice == 'MAR':
            st.write('## Março')
            callmes('MAR', url, clearScreen)
        
        if choice == 'ABR':
            st.write('## Abril')
            callmes('ABR', url, clearScreen)
        
        if choice == 'MAI':
            st.write('## Maio')
            callmes('MAI', url, clearScreen)

        if choice == 'JUN':
            st.write('## Junho')
            callmes('JUN', url, clearScreen)
        
        if choice == 'JUL':
            st.write('## Julho')
            callmes('JUL', url, clearScreen)

        if choice == 'AGO':
            st.write('## Agosto')
            callmes('AGO', url, clearScreen)

        if choice == 'SET':
            st.write('## Setembro')
            callmes('SET', url, clearScreen)

        if choice == 'OUT':
            st.write('## Outubro')
            callmes('OUT', url, clearScreen)

        if choice == 'NOV':
            st.write('## Novembro')
            callmes('NOV', url, clearScreen)

        if choice == 'DEZ':
            st.write('## Dezembro')
            callmes('DEZ', url, clearScreen)
        
        if choice == 'FEV05':
            st.write('## Fevereiro 05')
            callmes('FEV05', url, clearScreen)
        
        if choice == 'MAR05':
            st.write('## Março 05')
            callmes('MAR05', url, clearScreen)
    
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx FIM BODY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 



if __name__ == '__main__':
    main()