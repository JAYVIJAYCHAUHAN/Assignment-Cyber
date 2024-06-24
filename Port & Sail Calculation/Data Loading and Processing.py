 
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample Data
data = {
    'transaction_id': ['TRX001', 'TRX002', 'TRX003', 'TRX004', 'TRX005', 'TRX006', 'TRX007'],
    'date': ['2024-06-01', '2024-06-01', '2024-06-01', '2024-06-02', '2024-06-02', '2024-06-03', '2024-06-03'],
    'category': ['Food', 'Utilities', 'Entertainment', 'Food', 'Transport', 'Utilities', 'Food'],
    'amount': [25.00, 150.00, 200.00, 3000.00, 45.00, 135.00, 20.00]
}

df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Basic Data Cleaning
df.dropna(inplace=True)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df.dropna(inplace=True)
