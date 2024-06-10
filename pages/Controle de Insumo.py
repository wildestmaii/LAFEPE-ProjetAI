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
        dfGlobal = pd.read_csv("D:/Programação/#_Python/a/dados/copiainsumo.csv")
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
        limpeza_MAI = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'UtilizarJUN', 'Sobra/FaltaJUN',
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
        df_Mai = dfGlobal.drop(columns=limpeza_MAI)
        st.dataframe(df_Mai, height=700)
     
        # Converter a coluna para valores numéricos
        df_Mai['Sobra/FaltaMAI'] = pd.to_numeric(df_Mai['Sobra/FaltaMAI'], errors='coerce')

        # Filtrar os dados com base nas condições
        negative_values = df_Mai[df_Mai['Sobra/FaltaMAI'] < 0]['Sobra/FaltaMAI']
        zero_values = df_Mai[df_Mai['Sobra/FaltaMAI'] == 0]['Sobra/FaltaMAI']
        positive_values = df_Mai[df_Mai['Sobra/FaltaMAI'] > 0]['Sobra/FaltaMAI']

        # Contagem dos valores
        counts = {'Zero': len(zero_values),
                  'Negative': len(negative_values),
                  'Positive': len(positive_values)}

        # Criar o gráfico
        fig, ax = plt.subplots()
        categories = list(counts.keys())
        values = list(counts.values())

        sns.barplot(x=categories, y=values, ax=ax)
        ax.set_title('Distribuição dos Valores de Sobra/FaltaMAI')
        ax.set_xlabel('Categoria')
        ax.set_ylabel('Contagem')

        # Exibir o gráfico no Streamlit
        st.pyplot(fig)

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