import pandas as pd

# Read the DataFrames from CSV files
brands_df = pd.read_csv('Brands.csv')
products_df = pd.read_csv('Products.csv')
kpi_definitions_df = pd.read_csv('KPI Definitions.csv')
common_questions_df = pd.read_csv('Common Questions.csv')

# Merge the DataFrames on the Brand column
merged_df = pd.merge(brands_df, products_df, on='Brand', suffixes=['_x', '_y'])

# Calculate the total units sold for each model
merged_df['Total Units Sold'] = merged_df['Units_x'] + merged_df['Units_y']

# Sort the models by total units sold in descending order
top_selling_models = merged_df.sort_values('Total Units Sold', ascending=False)

# Print the top selling models
print(top_selling_models.head())