import streamlit as st

def display_query(title, query, language='python'):
    st.subheader(f"{title} Query:")
    st.code(query, language=language)
