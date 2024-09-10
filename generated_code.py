import pandas as pd

# Read the DataFrames from CSV files
brands_df = pd.read_csv('Brands.csv')
products_df = pd.read_csv('Products.csv')

# Merge the DataFrames on the Brand column
merged_df = pd.merge(brands_df, products_df, on='Brand')

# Calculate the percentage of sales via promotional sales for each brand
merged_df['Promo Sales %'] = merged_df['Revenue (EUR)_y'] / merged_df['Revenue (EUR)_x'] * 100

# Get the brand with the highest percentage of sales via promotional sales
highest_promo_sales_brand = merged_df['Brand'].loc[merged_df['Promo Sales %'].idxmax()]

# Print the brand with the highest percentage of sales via promotional sales
print(f"The brand with the highest percentage of sales via promotional sales is {highest_promo_sales_brand}.")