import streamlit as st
from query_generator import PythonQueryGenerator, SQLQueryGenerator,AnswerGenerator
from ui_components import display_query

def main():
    st.set_page_config(page_title="Hackathon Query Generator")
    st.header("Query Generator for Hackathon")
    python_generator = PythonQueryGenerator()
    sql_generator = SQLQueryGenerator()
    ans_generator=AnswerGenerator()

    question = st.text_input("Enter your question:", key="input")
    generate = st.button("Generate Queries")

    if generate and question:
        python_query = python_generator.generate_query(question)
        sql_query = sql_generator.generate_query(question)
        ans_query=ans_generator.generate_query(question)
        display_query('Your Answer',ans_query,'python')
        display_query('Python',python_query,'python')
        display_query('SQL',sql_query,'python')
       
        # st.subheader("Your Answer:")
        # st.code(python_query, language='text')
        
        # st.subheader("Your Answer:")
        # st.code(python_query, language='python')
        
        # st.subheader("SQL Query:")
        # st.code(sql_query, language='sql')

if __name__ == "__main__":
    main()
