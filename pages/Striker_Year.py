import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Striker per Year")

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

df = pd.read_csv('data/newTopGoalScorer.csv')

if option_entity == 'chart':
    fig, ax = plt.subplots(facecolor='#0e1117')

    ax.scatter(df.Year,df.Goals.sort_values(),color='#800080')
    ax.plot(df.Year,df.Goals.sort_values(),color='#800080')
    ax.set_title("Goals per Year",color='white')

    annotations = ['CR7','CR7','CR7','CR7','CR7','CR7','Messi','Lewan','Halland','Benzema']

    for xi,yi,text in zip(df.Year,df.Goals.sort_values(),annotations):
        ax.annotate(text,
                    xy=(xi, yi), xycoords='data',
                    xytext=(1.5, 1.5), textcoords='offset points')
    ax.tick_params(axis='x',colors='white')
    ax.tick_params(axis='y',colors='white')
    st.pyplot(fig)
else:
    st.dataframe(df)
