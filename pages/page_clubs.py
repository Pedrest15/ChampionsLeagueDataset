import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Clubs")

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

df = pd.read_csv('data/newAllTimeRankingByClub.csv')

if option_entity == 'chart':
    properities = list(df.columns)
    properities.remove('Club')
    properities.remove('Country')

    selected_properity = st.selectbox("Whitch properity do you wanna see?:", 
                                  properities)
    fig, ax = plt.subplots()

    ax.barh(df.Club,df[selected_properity], align='center')
    ax.set_title(selected_properity)
    st.pyplot(fig)
else:
    st.dataframe(df)
