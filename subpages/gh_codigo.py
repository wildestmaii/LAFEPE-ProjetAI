#MOSTRA A PROGRESSAO DO INSUMO AO LONGO DOS MESES DE ACORDO COM O CODIGO DELE

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def callcodigo(codigoMP, url, clearScreen):

    # Carregar o dataset (ajuste o caminho conforme necessário)
    #dfGlobal = pd.read_csv("D:/Programação/VSCode/praticando/pythonCRUD/crudpython/LAFEPE-ProjetAI/data/copiainsumo.csv")
    dfGlobal = pd.read_csv(url)
    dfGlobal['Código MP'] = dfGlobal['Código MP'].astype(str)

    # Filtrar as colunas relevantes
    escolha_colunas = [
        'Sobra/FaltaJAN04', 'Sobra/FaltaFEV', 'Sobra/FaltaMAR',
        'Sobra/FaltaABR', 'Sobra/FaltaMAI', 'Sobra/FaltaJUN',
        'Sobra/FaltaJUL', 'Sobra/FaltaAGO', 'Sobra/FaltaSET',
        'Sobra/FaltaOUT', 'Sobra/FaltaNOV', 'Sobra/FaltaDEZ', 
        'Sobra/FaltaFEV05', 'Sobra/FaltaMAR05'
    ]

    # Filtrar a linha que corresponde ao codigoMP
    df_Codigo = dfGlobal[dfGlobal['Código MP'] == codigoMP]
    
    # Verificar se o codigoMP foi encontrado
    if df_Codigo.empty:
        clearScreen.write(f'Código {codigoMP} não encontrado.')
        return
    
    # Selecionar os valores individuais para visualização
    dfVisu = df_Codigo[escolha_colunas].transpose().reset_index()
    dfVisu.columns = ['Mes', 'Sobra_Falta']

    # Ajustar os nomes dos meses
    dfVisu['Mes'] = [
        'JAN04', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 
        'FEV05', 'MAR05'
    ]

    # Converter valores para numéricos
    dfVisu['Sobra_Falta'] = pd.to_numeric(dfVisu['Sobra_Falta'], errors='coerce')

    # Plotar gráfico de barras
    plt.figure(figsize=(20, 8))
    plt.bar(dfVisu['Mes'], dfVisu['Sobra_Falta'], color=['green' if x >= 0 else 'red' for x in dfVisu['Sobra_Falta']])
    plt.axhline(0, color='black', linewidth=0.8)  # Linha no zero
    plt.xlabel('Meses')
    plt.ylabel('Quantidade')
    plt.title(f'Sobra ou Falta de Produtos por Mês para código {codigoMP}')
    plt.grid(True)
    plt.xticks(rotation=45)

    
    # Exibir os dados filtrados no Streamlit
    dfCd = df_Codigo[escolha_colunas]
    clearScreen.dataframe(dfCd, use_container_width=True)
    # Exibir o gráfico no Streamlit
    st.pyplot(plt)



# Exemplo de chamada da função
#callcodigo('10') 