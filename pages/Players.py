import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Striker Players")

# CSS to inject contained in a string
hide_table_row_index = """
                            <style>
                            thead tr th:first-child {display:none}
                            tbody th {display:none}
                            </style>
                            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

option_entity = st.radio('Options:', ('chart', 'spreadsheet'), horizontal=False)

df = pd.read_csv('data/newPlayerGoalTotals.csv')

if option_entity == 'chart':
    fig, ax = plt.subplots(facecolor='#0e1117')

    ax.barh(df.Player,df.Goals, align='center',color='#800080')
    ax.set_xticks(df.Goals,color='white')
    ax.tick_params(axis='x',colors='white')
    ax.tick_params(axis='y',colors='white')
    ax.set_title("Goals", color='white')
    st.pyplot(fig)
else:
    st.dataframe(df)
