import google.generativeai as genai
import langchain
import pandas as pd  # Import pandas for database operations
import re
import openpyxl
import streamlit as st
from contextlib import redirect_stdout
import io
import subprocess
from code_editor import code_editor
# Creating separate DataFrames for each sheet in the Excel file

brands_df = pd.read_csv('Brands.csv')
products_df = pd.read_csv('Products.csv')
kpi_definitions_df = pd.read_csv('KPI definitions.csv')
common_questions_df = pd.read_csv('Common questions.csv')

genai.configure(api_key="AIzaSyCxs4c6qTKAN1Xi5rwTxS1WbQjVwZ4_1rs")
generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]


model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Start conversation with user input
convo = model.start_chat(history=[
    {"role": "user", "parts": ["""You are a python code generator,I have a dataset containing sales performance metrics for various product models and brands, structured in different pandas DataFrames after reading from corresponding CSV files. I need Python code to analyze this data. The DataFrames and their respective columns are as follows:

{brands_df} from Brands.csv:

Columns: Brand, Revenue (EUR), Revenue Change (%), Revenue Change (EUR), Units, Units Change (%), Units Change, Price (EUR), Price Change (%), Price Change (EUR), Price index, Price index Change
{products_df} from Products.csv:

Columns: Model code, Brand, Revenue (EUR), Revenue Change (%), Revenue Change (EUR), Units, Units Change (%), Units Change, Price (EUR), Price Change (%), Price Change (EUR), Price index, Price index Change, Act. Num. Dist., Act. Num. Dist. Change (pp), TPR units, TPR units Change (%), TPR units Change
{kpi_definitions_df} from KPI Definitions.csv:

Contains the detailed descriptions of each KPI used in the dataset.
Columns: [You need to insert the correct column names based on your KPI Definitions sheet]
{common_questions_df} from Common Questions.csv:

A compilation of frequently asked questions regarding sales data.
Columns: [You need to insert the correct column names based on your Common Questions sheet]
Based on the above DataFrames, :
Please generate the Python code to perform these analyses using pandas."""]},
    {
    "role": "model",
    "parts": [""]
    },
     {"role": "user", "parts": ["""Your python code should be importing all the necessary imports and necessary methods to calculate the final solution and every variable should be defined properly  """]},
    {
    "role": "model",
    "parts": [""]
    },
    
     {"role": "user", "parts": ["""when merging these DataFrames, columns with the same name in both DataFrames have been suffixed with _x and _y to differentiate them,After merging these DataFrames on the Brand column, columns from brands_df are suffixed with _x and those from products_df with _y also Since 'Brand' does not have a suffix, use it directly. 'Model code' is also directly used as it's unique to products_df. Make sure you are using correct suffix _x and _y with correct columns name include space and brakcets if its there in the column names, do accurately with full column names toa void mistake because this is very crucial and  leading to so many errors """]},
    {
    "role": "model",
    "parts": [""]
    }
    ,
    
     {"role": "user", "parts": ["""It is very important for my carrier please do not make mistake while generating the python code and formula with column names and if question is a normal conversation then please ask politely to ask question realted to database only """]},
    {
    "role": "model",
    "parts": [""]
    }
])

####Streamlit App


if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_stage(stage):
    st.session_state.stage = stage

st.set_page_config(
    page_title="Hackathon - Challenge #3",
    page_icon="artificial-intelligence.png",
    layout="centered",
    initial_sidebar_state="auto",

)
about_content = """
        ## Hackathon Challenge #3

        This app is developed for the Hackathon Challenge #3. It showcases the ability to dynamically generate and execute Python code based on user input, offering a blend of advanced data processing and interactive elements.

        Features include:
        - **Dynamic Python Code Generation**: Leveraging a language model to convert natural language questions into executable Python code.
        - **Editable Code Output**: Users can view, edit, and re-run the generated code, enhancing the learning and debugging experience.
        - **Interactive Data Exploration**: With the generated code, users can interact with and analyze the sample data provided in the hackathon dataset.

        This is an AI app designed to make data analysis more accessible and engaging!
 

               """

st.sidebar.markdown(about_content)
st.header("APP for your solution")
question = st.text_input("Input:",key="input")
submit = st.button("Ask the question",on_click=set_stage, args=(1,))
submit_button=[{
   
   "commands": ["submit"],

 }]
if st.session_state.stage > 0:
    convo.send_message(question)
    generated_code=convo.last.text
    pattern = r'^```python\n(.+?)\n```$'
    replacement = r'\1'
    generated_code_new = re.sub(pattern, replacement, generated_code, flags=re.DOTALL)
    generated_code_new=f"""{generated_code_new}"""
    print(generated_code_new)
    file_path = 'generated_code.py'
    with open(file_path, 'w') as file:
        file.write(generated_code_new)
        print(f"Successfully written to {file_path}")
    
        
    with open(file_path, "r") as file:
        python_code_from_file = file.read()

    def execute_and_capture(script_path):
        """Executes a given Python script and captures its output."""
        try:
            # Execute the script and capture output
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return e.stdout, e.stderr
    def display_execution_output(stdout, stderr):
        
        if stdout:
            st.subheader('Output:')
            st.code(stdout, language='python')  # Using st.code for syntax highlighting
        
        if stderr:
            st.subheader('Error:')
            st.error(stderr)
    script_path = "c:/Users/kuka2004/Desktop/Hackathon/generated_code.py"

    stdout, stderr = execute_and_capture(script_path)
    display_execution_output(stdout, stderr)

    with st.expander("Open to view code"):
        with open(file_path, "r") as file:
            python_code_from_file = file.read()
        print(python_code_from_file,type(python_code_from_file))
        edited_code= code_editor(python_code_from_file, height=300,key='code_editor')
        print("edited_code",edited_code)
        #edited_code = st.text_area("Edit the code below:", value=python_code_from_file, height=300)
        #st.code(edited_code, language='python')
       
        user_code = edited_code['text']
        if st.button('Save and Run Edited Code',on_click=set_stage, args=(2,)):
            with open(file_path, "w") as file:
                    file.write(user_code)
        if st.session_state.stage > 1:
            st.success("Code saved successfully. Re-executing...")
            stdout, stderr = execute_and_capture(script_path)
            display_execution_output(stdout, stderr)
# Use Streamlit columns to create a layout that pushes the button to the right
 # Adjust the ratio as needed for your layout

 # This places the button in the second column, which is pushed to the right
if st.button('Refresh This Session'):
        # Reset the session state or specific variables
    for key in st.session_state.keys():
        del st.session_state[key]
        # Rerun the app from the top
    st.rerun()

            

   
            
        
    