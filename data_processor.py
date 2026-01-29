import pandas as pd
import os

# 1. Files to process
data_files = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

combined_data = []

for file in data_files:
    # Read CSV
    df = pd.read_csv(file)
    
    # 2. Filter for pink morsels 
    df = df[df['product'].str.lower() == 'pink morsel']
    
    # 3. Calculate sales
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['sales'] = df['price'] * df['quantity']
    
    # 4. Keep necessary columns
    df = df[['sales', 'date', 'region']]
    
    combined_data.append(df)

# 5. Concatenate all dataframes into one
final_df = pd.concat(combined_data)

# 6. CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Success! 'formatted_data.csv' has been created.")