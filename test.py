import streamlit as st
import pandas as pd
import numpy as np


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

chart_data2 = pd.DataFrame(
   {
       "col1": np.random.randn(20),
       "col2": np.random.randn(20),
       "col3": np.random.choice(["A", "B", "C"], 20),
   }
)

st.line_chart(chart_data2, x="col1", y="col2", color="col3")

# para iniciar o código, digite no terminal: streamlit run test.py