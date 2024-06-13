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

   
    fig, ax = plt.subplots()
    fig = plt.figure(figsize=(3.7, 2))
    ax = fig.add_subplot(111)
    categories = list(counts.keys())
    values = list(counts.values())

    sns.barplot(x=categories, y=values, ax=ax, color='#8602f3', zorder=4)
    fig.patch.set_facecolor('none')
    ax.set_facecolor('none')
    ax.set_title('' + mes.lower(), fontsize=6, color='#9B9DAB')
    ax.set_xlabel('Categoria', fontsize=6, color='#9B9DAB')
    ax.set_ylabel('Contagem', fontsize=6, color='#9B9DAB')
    ax.tick_params(axis='x', labelsize=6, colors='#9B9DAB', length=1)  # Tamanho das labels dos ticks do eixo X
    ax.tick_params(axis='y', labelsize=6, colors='#9B9DAB', length=1) 
    ax.grid(True, axis='y', color='#9B9DAB', linewidth=0.3, zorder=0)

    #plt.setp(ax.get_xticklabels(), fontweight='bold')
    #plt.setp(ax.get_yticklabels(), fontweight='bold')
    ax = plt.gca()  # Obter o objeto Axes atual
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # Exibir o gráfico no Streamlit
    st.pyplot(fig)






