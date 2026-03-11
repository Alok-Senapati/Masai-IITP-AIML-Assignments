import numpy as np
import pandas as pd

sales_records = [
    {'product_id': 'P001', 'product_name': 'Laptop', 'category': 'Electronics', 'price': 1200, 'quantity': 5},
    {'product_id': 'P002', 'product_name': 'Mouse', 'category': 'Electronics', 'price': 25, 'quantity': 50},
    {'product_id': 'P003', 'product_name': 'Desk', 'category': 'Furniture', 'price': 350, 'quantity': 10},
    {'product_id': 'P004', 'product_name': 'Chair', 'category': 'Furniture', 'price': 150, 'quantity': 20},
    {'product_id': 'P005', 'product_name': 'Monitor', 'category': 'Electronics', 'price': 400, 'quantity': 8}
]


lookup_dictionary = {record['product_id']: record['product_name'] for record in sales_records}
products_with_price_more_than_100 = [record['product_name'] for record in sales_records if record['price'] > 100]
total_value_dictionary = {record['product_id']: record['price'] * record['quantity'] for record in sales_records}
print(f"Lookup Dictionary: {lookup_dictionary}")
print(f"Products with price > 100: {products_with_price_more_than_100}")
print(f"Product total revenue: {total_value_dictionary}")

product_id_arr = np.array([record['product_id'] for record in sales_records])
price_arr = np.array([record['price'] for record in sales_records])
quantity_arr = np.array([record['quantity'] for record in sales_records])
total_revenue = price_arr * quantity_arr
idx_highest_revenue = np.argmax(total_revenue)
avg_revenue = np.mean(total_revenue)
products_greater_than_average = product_id_arr[total_revenue > avg_revenue]
print(f"Total Revenue: {total_revenue}")
print(f"Index of highest revenue: {idx_highest_revenue}")
print(f"Average revenue: {avg_revenue}")
print(f"Products having revenue more than average: {products_greater_than_average}")

sales_df = pd.DataFrame(sales_records)
sales_df["revenue"] = sales_df["price"] * sales_df["quantity"]
print(sales_df.head())

## Advantage of Dataframes
"""
Using a DataFrame with labeled columns is better because it provides 
clear column names, making the data easier to read, understand, and analyze 
compared to a plain NumPy array with only positional indexing.

DataFrames also support powerful built-in operations like grouping, filtering, and aggregation
directly on labeled data, which simplifies analysis. Additionally, they handle missing values 
and mixed data types more effectively. This improves both data management and code readability.
"""