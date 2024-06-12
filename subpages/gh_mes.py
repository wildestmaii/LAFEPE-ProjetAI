#SE NAQUELE MÊS TEVE MAIS FALTAS OU SOBRA DE INSUMOS
import streamlit as st        
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def callmes(mes, url, clearScreen):
    #container = st.container(border=True)
    dfGlobal = pd.read_csv(url)
 
    # Correção: Definir escolha_MES como uma string, não uma lista
    escolha_MES = 'Sobra/Falta'+mes

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


    #width = st.sidebar.slider("plot width", 0.1, 25., 3.)
    #height = st.sidebar.slider("plot height", 0.1, 25., 1.)


    #st.markdown("<h1 style='text-align: center; color: #000;'>Distribuição dos Valores de Sobra/Falta </h1>", unsafe_allow_html=True)
    
    
    # Criar o gráfico
    #fig, ax = plt.subplots(figsize=(width, height))
   
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(4, 1.5))
    ax = fig.add_subplot(111)
    categories = list(counts.keys())
    values = list(counts.values())

    sns.barplot(x=categories, y=values, ax=ax)
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    ax.set_title('Distribuição dos Valores de Sobra/Falta ' + mes, fontsize=5)
    ax.set_xlabel('Categoria', fontsize=6)
    ax.set_ylabel('Contagem', fontsize=6)
    ax.tick_params(axis='x', labelsize=5)  # Tamanho das labels dos ticks do eixo X
    ax.tick_params(axis='y', labelsize=5) 
    ax.grid(True, color='#FDFCFC',  linewidth=0.4)
    # Exibir o gráfico no Streamlit
    st.pyplot(fig)







    # Criar o gráfico de linha
    #fig, ax = plt.subplots()
    #categories = list(counts.keys())
    #values = list(counts.values())

    #ax.plot(categories, values, marker='o', linestyle='-', color='b')
    #ax.set_title('Distribuição dos Valores de Sobra/Falta ' + mes)
    #ax.set_xlabel('Categoria')
    #ax.set_ylabel('Contagem')

    # Exibir o gráfico no Streamlit
    #st.pyplot(fig,)

# Exemplo de chamada da função
#callmes('FEV')
