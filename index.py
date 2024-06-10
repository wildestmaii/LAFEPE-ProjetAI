import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# importação do csv
validade = pd.read_csv('/workspaces/LAFEPE-ProjetAI/data/validade.csv', sep=",")

# preparação do dataframe
df_lote1 = validade[['Código MP', 'UND', 'Lote 01', 'Quantidade', 'Custo Unit.', 'Validade', 'Prev. de Consumo', 'Status']]
df_lote2 = validade[['Código MP', 'UND', 'Lote 02', 'Quantidade2', 'Custo Unit.2', 'Validade2', 'Prev. de Consumo2', 'Status']]
df_lote3 = validade[['Código MP', 'UND', 'Lote 03', 'Quantidade3', 'Custo Unit3', 'Validade3', 'Prev. de Consumo3', 'Status']]
df_lote4 = validade[['Código MP', 'UND', 'Lote 04', 'Quantidade4', 'Custo Unit4', 'Validade4', 'Prev. de Consumo4', 'Status']]

# renomeando colunas para visualização
df_lote1.columns = ['Código MP', 'UND', 'Lote', 'Quantidade', 'Custo Unit.', 'Validade', 'Prev. de Consumo', 'Status']
df_lote2.columns = ['Código MP', 'UND', 'Lote', 'Quantidade', 'Custo Unit.', 'Validade', 'Prev. de Consumo', 'Status']
df_lote3.columns = ['Código MP', 'UND', 'Lote', 'Quantidade', 'Custo Unit.', 'Validade', 'Prev. de Consumo', 'Status']
df_lote4.columns = ['Código MP', 'UND', 'Lote', 'Quantidade', 'Custo Unit.', 'Validade', 'Prev. de Consumo', 'Status']

# seleção




"""
# Visão Geral
"""
# demonstra todos os dados
st.dataframe(validade, use_container_width=True)


"""
### Análise do status de consumo: Geral
"""
# Extrair e combinar colunas de status dos lotes
status_columns = ['Status', 'Status.1', 'Status.2', 'Status.3']
statuses = validade[status_columns].stack().reset_index(drop=True)

# Contar a soma de cada status
status_counts = statuses.value_counts()

# Criar o gráfico de pizza
fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Assegura que o gráfico é desenhado como um círculo
st.pyplot(fig)


"""
# Primeiro Lote
"""
st.dataframe(df_lote1, use_container_width=True)


"""
### Análise do status de consumo: Primeiro Lote
"""
status_counts = df_lote1['Status'].value_counts()

# Criar gráfico de pizza
fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)


"""
### Análise da Validade vs Previsão de consumo vs Status
"""
fig, ax = plt.subplots()
df_lote1[['Validade', 'Prev. de Consumo']].plot(kind='bar', ax=ax)
ax.set_xticklabels(df_lote1['Código MP'])
ax.set_xlabel('Código MP')
ax.set_ylabel('Data')
ax.set_title('Comparação entre Validade e Prev. de Consumo')
st.pyplot(fig)


"""
# Segundo Lote
"""




"""
# Terceiro Lote
"""




"""
# Quarto Lote
"""



