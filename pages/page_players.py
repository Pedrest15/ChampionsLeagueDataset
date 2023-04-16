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
    fig, ax = plt.subplots()

    ax.barh(df.Player,df.Goals, align='center')
    ax.set_xticks(df.Goals)
    ax.set_title("Goals")
    st.pyplot(fig)
else:
    st.dataframe(df)