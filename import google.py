import pandas as pd
import numpy as np

brands_df = pd.read_csv('Brands.csv')
products_df = pd.read_csv('Products.csv')
print(products_df.head(5))
kpi_definitions_df = pd.read_csv('KPI Defintions.csv')
common_questions_df = pd.read_csv('Common Questions.csv')

# 1. Identify the product model that has the highest Revenue (EUR) from the products_df DataFrame.
highest_revenue_product = products_df['Model code'][products_df['Revenue (EUR)'].idxmax()]
print("Product model with the highest Revenue (EUR):", highest_revenue_product)

# 2. Calculate the total Revenue (EUR) for each brand from the brands_df DataFrame and identify which brand has the highest total revenue.
brands_df['Total Revenue (EUR)'] = brands_df['Revenue (EUR)']
highest_revenue_brand = brands_df['Brand'][brands_df['Total Revenue (EUR)'].idxmax()]
print("Brand with the highest total Revenue (EUR):", highest_revenue_brand)

# 3. Understand the relationship between the Act. Num. Dist. and Units sold from the products_df DataFrame. Specifically, calculate the correlation coefficient between these two columns.
correlation = products_df['Act. Num. Dist.'].corr(products_df['Units'])
print("Correlation coefficient between Act. Num. Dist. and Units:", correlation)

# 4. Which brands are budget brands (operating at lower end of the market in terms of pricing)?
budget_brands = brands_df[brands_df['Price (EUR)'] < brands_df['Price (EUR)'].mean()]
print("Budget brands:", budget_brands['Brand'].tolist())
