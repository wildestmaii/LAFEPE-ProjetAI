import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

validade = pd.read_csv('/workspaces/LAFEPE-ProjetAI/data/validade.csv', sep=",")
st.dataframe(validade, use_container_width=True)

"""
# Primeiro Trimestre
"""
validade_primeiro_trimestre = validade['Código MP'], validade['UND'], validade['Lote 01'], validade['Quantidade'], validade['Custo Unit.'], validade['Validade'], validade['Prev. de Consumo'], validade['Status']
st.dataframe(validade_primeiro_trimestre, use_container_width=True)



"""
# Segundo Trimestre
"""
# validade_segundo_trimestre = 



"""
# Terceiro Trimestre
"""
# validade_terceiro_trimestre = 



"""
# Quarto Trimestre
"""
# validade_quarto_trimestre = 



