import pandas as pd
import numpy as np


orders = pd.DataFrame({
    'order_id': ['R01', 'R02', 'R03', 'R04', 'R05', 'R06', 'R07', 'R08', 'R01'],
    'customer_id': ['K1', 'K2', 'K3', 'K1', 'K4', 'K2', 'K5', 'K3', 'K1'],
    'product_id': ['W01', 'W02', 'W03', 'W04', 'W05', 'W01', 'W02', 'W03', 'W01'],
    'quantity': [2, 1, 3, 1, 2, 4, 1, 2, 2]
})

customers = pd.DataFrame({
    'customer_id': ['K1', 'K2', 'K3', 'K4', 'K5'],
    'name': ['  ravi KUMAR ', 'SITA sharma', 'amit PATEL', 'Neha Gupta', 'POOJA singh'],
    'region': ['north', 'SOUTH', ' West', 'North', 'south']
})

products = pd.DataFrame({
    'product_id': ['W01', 'W02', 'W03', 'W04', 'W05'],
    'product_name': ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E'],
    'category': ['Electronics', 'Clothing', None, 'Electronics', 'Clothing'],
    'price': ['Rs. 500', 'Rs. 300', 'Rs. 800', 'Rs. 1200', 'Rs. 450']
})
