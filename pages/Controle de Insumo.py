#g) Controle da validade dos insumos.
#h) Sinalização dos insumos mais próximos do vencimento.
import streamlit as st
import pandas as pd

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#st.title("Controle de Insumos")
st.markdown("<h1 style='text-align: center; color: #fff;'>Controle de Insumos</h1>", unsafe_allow_html=True)
dfGlobal = pd.read_csv("/workspaces/LAFEPE-ProjetAI/data/consolidacaoestoque.csv")  # read a CSV file


# --- SIDEBAR
#if (dfGlobal is not None):
    #bank = dfGlobal.copy()

    #with st.sidebar.form(key='my_form'):

        # SELECIONA O TIPO DE GRÁFICO
        #graph_type = st.radio('Tipo de gráfico:', ('Barras', 'Pizza'))
        
        # MÊS 
        #month_list = bank.month.unique().tolist()
        #month_list.append('')
        #month_selected =  st.multiselect("Mês do contato", month_list, [''])

menu = ['Global', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ',]
choice = st.sidebar.selectbox("Menu", menu)


# --- FIM SIDEBAR 



# --- BODY

# RENOMEAR
#rename_colunas = {
#    'Código MP': 'Cod',
#    'Estoque': 'Estoque',
#    'UND': 'Und',
#    'Quarentena': 'Quarentena',
#    'Validade ¹': 'Validade',
#    'A UtilizarFev': 'UtilzarFEv',
#    'A UtilizarMAI': 'UtilizarMAI'
#}

# Aplicando a renomeação das colunas
#dfGlobal = dfGlobal.rename(columns=rename_colunas)


# LIMPEZA 
limpeza_JAN = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN',
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Jan = dfGlobal.drop(columns=limpeza_JAN)

limpeza_FEV = ['UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN',
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Fev = dfGlobal.drop(columns=limpeza_FEV)

limpeza_MAR = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN',
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Mar = dfGlobal.drop(columns=limpeza_MAR)

limpeza_ABR = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
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
df_Abr = dfGlobal.drop(columns=limpeza_ABR)

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

limpeza_JUN = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
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
df_Jun = dfGlobal.drop(columns=limpeza_JUN)

limpeza_JUL = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
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
df_Jul = dfGlobal.drop(columns=limpeza_JUL)

limpeza_AGO = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Ago = dfGlobal.drop(columns=limpeza_AGO)

limpeza_SET = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Set = dfGlobal.drop(columns=limpeza_SET)

limpeza_OUT = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Out = dfGlobal.drop(columns=limpeza_OUT)

limpeza_NOV = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO', 
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarDEZ', 'Sobra/FaltaDEZ',
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Nov = dfGlobal.drop(columns=limpeza_NOV)

limpeza_DEZ = ['A UtilizarFEV', 'Sobra/FaltaFEV',
               'UtilizarMAR', 'Sobra/FaltaMAR',
               'UtilizarABR', 'Sobra/FaltaABR',
               'A UtilizarMAI', 'Sobra/FaltaMAI',
               'UtilizarJUN', 'Sobra/FaltaJUN', 
               'UtilizarJUL', 'Sobra/FaltaJUL', 
               'UtilizarAGO', 'Sobra/FaltaAGO',
               'UtilizarSET', 'Sobra/FaltaSET', 
               'UtilizarOUT', 'Sobra/FaltaOUT', 
               'UtilizarNOV', 'Sobra/FaltaNOV', 
               'UtilizarJAN04', 'Sobra/FaltaJAN04',
               'UtilizarFEV05', 'Sobra/FaltaFEV05',
               'UtilizarMAR05', 'Sobra/FaltaMAR05',
               'SimulacaoUtilizar', 'SimulacaoSobra/Falta',
               'UND', 'Validade ¹']
df_Dez = dfGlobal.drop(columns=limpeza_DEZ)




# Excluir as colunas
def main():
    if choice == 'Global':
        st.write('## Global')
        st.dataframe(dfGlobal, height=700, width=1000, use_container_width=False)

    if choice == 'JAN':
        st.write('## Janeiro')
        #st.line_chart(st.dataframe(df_Jan))
        st.dataframe(df_Jan, height=700)

    if choice == 'FEV':
        st.write('## Fevereiro')
        st.dataframe(df_Fev, height=700)

    if choice == 'MAR':
        st.write('## Março')
        st.dataframe(df_Mar, height=700)
    
    if choice == 'ABR':
        st.write('## Abril')
        st.dataframe(df_Abr, height=700)
    
    if choice == 'MAI':
        st.write('## Maio')
        st.dataframe(df_Mai, height=700)
    
    if choice == 'JUN':
        st.write('## Junho')
        st.dataframe(df_Jun, height=700)
    
    if choice == 'JUL':
        st.write('## Julho')
        st.dataframe(df_Jul, height=700)

    if choice == 'AGO':
        st.write('## Agosto')
        st.dataframe(df_Ago, height=700)

    if choice == 'SET':
        st.write('## Setembro')
        st.dataframe(df_Set, height=700)

    if choice == 'OUT':
        st.write('## Outubro')
        st.dataframe(df_Out, height=700)

    if choice == 'NOV':
        st.write('## Novembro')
        st.dataframe(df_Nov, height=700)

    if choice == 'DEZ':
        st.write('## Dezembro')
        st.dataframe(df_Dez, height=700)

# -- FIM BODY



if __name__ == '__main__':
    main()