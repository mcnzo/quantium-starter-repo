import pandas as pd
import os

# 1. Define the files to process
data_files = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

combined_data = []

for file in data_files:
    # Read the CSV
    df = pd.read_csv(file)
    
    # 2. Filter for only Pink Morsels (case-insensitive just in case)
    df = df[df['product'].str.lower() == 'pink morsel']
    
    # 3. Calculate Sales (remove the '$' from price first, then convert to float)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Keep only the necessary columns
    df = df[['sales', 'date', 'region']]
    
    combined_data.append(df)

# 5. Concatenate all dataframes into one
final_df = pd.concat(combined_data)

# 6. Export to a single CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Success! 'formatted_data.csv' has been created.")