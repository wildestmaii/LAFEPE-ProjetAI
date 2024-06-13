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


url = "data/insumo.csv"

clearScreen = st.empty()

# ---------------------------------- FIM HEADER -----------------------------------

#dados gerais do controle de insumos
dfGlobal = pd.read_csv(url)
dfGlobal['Código MP'] = dfGlobal['Código MP'].astype(str)
clearScreen.write('### Dados Gerais')
st.dataframe(dfGlobal)
st.divider()


col1, col2 = st.columns([0.4, 0.6])
with col1:

    with st.container(border=True, height=570):
        st.markdown("""<h4>Distribuição dos valores de sobra/falta</h4>""",unsafe_allow_html=True)
        st.markdown("""<div class="divider2"></div>""",unsafe_allow_html=True)
        menu = [ 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'FEV05', 'MAR05']
        choice = st.selectbox("Selecione o mês que deseja visualizar:", menu)

        if choice == 'JAN':
            st.markdown("""<h5 class="titulo_meses">Janeiro</h5>""",unsafe_allow_html=True)
            callmes("JAN04", url, clearScreen)

        if choice == 'FEV':
            st.markdown("""<h5 class="titulo_meses">Fevereiro</h5>""",unsafe_allow_html=True)
            callmes('FEV', url, clearScreen)

        if choice == 'MAR':
            st.markdown("""<h5 class="titulo_meses">Março</h5>""",unsafe_allow_html=True)
            callmes('MAR', url, clearScreen)
        
        if choice == 'ABR':
            st.markdown("""<h5 class="titulo_meses">Abril</h5>""",unsafe_allow_html=True)
            callmes('ABR', url, clearScreen)
        
        if choice == 'MAI':
            st.markdown("""<h5 class="titulo_meses">Maio</h5>""",unsafe_allow_html=True)
            callmes('MAI', url, clearScreen)

        if choice == 'JUN':
            st.markdown("""<h5 class="titulo_meses">Junho</h5>""",unsafe_allow_html=True)
            callmes('JUN', url, clearScreen)
        
        if choice == 'JUL':
           st.markdown("""<h5 class="titulo_meses">Julho</h5>""",unsafe_allow_html=True)
           callmes('JUL', url, clearScreen)

        if choice == 'AGO':
            st.markdown("""<h5 class="titulo_meses">Agosto</h5>""",unsafe_allow_html=True)
            callmes('AGO', url, clearScreen)

        if choice == 'SET':
            st.markdown("""<h5 class="titulo_meses">Setembro</h5>""",unsafe_allow_html=True)
            callmes('SET', url, clearScreen)

        if choice == 'OUT':
            st.markdown("""<h5 class="titulo_meses">Outubro</h5>""",unsafe_allow_html=True)
            callmes('OUT', url, clearScreen)

        if choice == 'NOV':
            st.markdown("""<h5 class="titulo_meses">Novembro</h5>""",unsafe_allow_html=True)
            callmes('NOV', url, clearScreen)

        if choice == 'DEZ':
            st.markdown("""<h5 class="titulo_meses">Dezembro</h5>""",unsafe_allow_html=True)
            callmes('DEZ', url, clearScreen)
        
        if choice == 'FEV05':
            st.markdown("""<h5 class="titulo_meses">Fevereiro 05</h5>""",unsafe_allow_html=True)
            callmes('FEV05', url, clearScreen)
        
        if choice == 'MAR05':
            st.markdown("""<h5 class="titulo_meses">Março 05</h5>""",unsafe_allow_html=True)
            callmes('MAR05', url, clearScreen)

with col2:

    with st.container(border=True, height=570):
        st.markdown("""<h4>Sobra ou Falta de produtos por mês para o código especifico</h4>""",unsafe_allow_html=True)
        st.markdown("""<div class="divider2"></div>""",unsafe_allow_html=True)
        query = st.text_input(
                "Entre com o Código do Insumo especifico:",
                placeholder="This is a placeholder")
        if query:
          #clearScreen.write('query')
          callcodigo(query, url, clearScreen)

