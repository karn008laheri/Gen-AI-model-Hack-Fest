import pandas as pd

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_data(self):
        # Example of loading an Excel file with multiple sheets
        excel_data = pd.read_excel(self.file_path, sheet_name=None)
        return excel_data
