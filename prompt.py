from models import getModel
from data_manager import DataManager
model=getModel("gemini-1.0-pro")
file_path='AI Example data sets for hackathon.xlsx'
data_manager= DataManager(file_path)
data=data_manager.load_data()
brands_df = data['Brands'].dropna(how='all').reset_index(drop=True)
products_df = data['Products'].dropna(how='all').reset_index(drop=True)
kpi_definitions_df = data['KPI defintions'].dropna(how='all').reset_index(drop=True)
common_questions_df = data['Common questions'].dropna().reset_index(drop=True)
products_df=data['Products']

class prompting():
    def __init__(self):
        # Initialize any necessary attributes
        pass
    def python_conversation(self):
        convo = model.start_chat(history=[
            {"role": "user", "parts": ["""You are an expert in converting the natural language question to Python code for the question using the different dataframes """]},
            {
            "role": "model",
            "parts": [""]
            },
            {"role": "user", "parts": ["""Your python code should be importing all the necessary imports and necessary methods to calculate the final solution and every variable should be defined properly  """]},
            {
            "role": "model",
            "parts": [""]
            },
            
            {"role": "user", "parts": ["""and should only understand from the {brands_df},{products_df} and definitions of all columns from {kpi_definitions_df} and these three are already defined so do not redefine it"""]},
            {
            "role": "model",
            "parts": [""]
            },
        ])
        return convo
    def sql_conversation(self):
        convo = model.start_chat(history=[
            {"role": "user", "parts": ["""You are an expert in converting the natural language question to sql query for the question using the different dataframes """]},
            {
            "role": "model",
            "parts": [""]
            },
            {"role": "user", "parts": ["""Your sql query should be importing all the necessary imports and necessary methods to calculate the final solution, it should ask to repeat question if needed """]},
            {
            "role": "model",
            "parts": [""]
            },
            
            {"role": "user", "parts": ["""and should only understand from the {brands_df},{products_df} and definitions of all columns from {kpi_definitions_df} and these three are already defined so do not redefine it"""]},
            {
            "role": "model",
            "parts": [""]
            },
        ])
        return convo
    def ans_conversation(self):
        convo=model.start_chat(history=[
            {"role": "user", "parts": ["""You are an expert in solving the problems asked from the user and please give only the answer output of the solution by filling the data and doing the calculation, expectaion is the final answer to that question """]},
            {
            "role": "model",
            "parts": [""]
            },
            {"role": "user", "parts": ["""Please, do not mask the solution, you can give the name of the brands or revenue but answer of the question should be relevant to the provided data only  {brands_df},{products_df} and definitions of all columns from {kpi_definitions_df}, reply I dont know if you dont know """]},
            {
            "role": "model",
            "parts": [""]
            },
            
        ])
        return convo