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
    fig, ax = plt.subplots()

    ax.scatter(df.Year,df.Goals)
    ax.plot(df.Year,df.Goals)
    ax.set_title("Goals per Year")

    annotations = ['CR7','CR7','CR7','CR7','CR7','CR7','Messi','Lewan','Halland','Benzema']

    for xi,yi,text in zip(df.Year,df.Goals,annotations):
        ax.annotate(text,
                    xy=(xi, yi), xycoords='data',
                    xytext=(1.5, 1.5), textcoords='offset points')
    st.pyplot(fig)
else:
    st.dataframe(df)