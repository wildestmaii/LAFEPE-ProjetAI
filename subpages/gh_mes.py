import streamlit as st        
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def callmes(mes):
    st.write(mes)

    dfGlobal = pd.read_csv("D:/Programação/#_Python/a/dados/consolidacaoestoque.csv")

    # Correção: Definir escolha_MES como uma string, não uma lista
    escolha_MES = 'Sobra/Falta' + mes

    # Selecionar a coluna específica e colocar em um DataFrame
    df_Mes = dfGlobal[[escolha_MES]].copy()

    # Converter a coluna para valores numéricos
    df_Mes[escolha_MES] = pd.to_numeric(df_Mes[escolha_MES], errors='coerce')

    # Filtrar os dados com base nas condições
    negative_values = df_Mes[df_Mes[escolha_MES] < 0][escolha_MES]
    zero_values = df_Mes[df_Mes[escolha_MES] == 0][escolha_MES]
    positive_values = df_Mes[df_Mes[escolha_MES] > 0][escolha_MES]

    # Contagem dos valores
    counts = {
        'Zero': len(zero_values),
        'Negative': len(negative_values),
        'Positive': len(positive_values)
    }

    # Criar o gráfico de linha
    fig, ax = plt.subplots()
    categories = list(counts.keys())
    values = list(counts.values())

    ax.plot(categories, values, marker='o', linestyle='-', color='b')
    ax.set_title('Distribuição dos Valores de Sobra/Falta ' + mes)
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Contagem')

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)

# Exemplo de chamada da função
#callmes('FEV')