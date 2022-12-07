import streamlit as st
from main_page import data

st.title('this is the first page')

st.write(data.head(10))

