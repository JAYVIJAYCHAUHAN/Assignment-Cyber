import pandas as pd
import numpy as np
from scipy import stats

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

# Group by category and calculate statistics
stats_df = df.groupby('category')['amount'].agg(['mean', 'median', 'std', 'count']).reset_index()

# Anomaly detection function
def detect_anomalies(df, stats_df):
    anomalies = []
    
    for index, row in df.iterrows():
        category_stats = stats_df[stats_df['category'] == row['category']].iloc[0]
        mean = category_stats['mean']
        std_dev = category_stats['std']
        
        if std_dev == 0:
            continue
        
        z_score = (row['amount'] - mean) / std_dev
        
        if np.abs(z_score) > 3:  # Using 3 standard deviations as the threshold
            anomalies.append({
                'transaction_id': row['transaction_id'],
                'date': row['date'],
                'category': row['category'],
                'amount': row['amount'],
                'reason_for_anomaly': f'{z_score:.2f} standard deviations from the mean'
            })
    
    return anomalies

# Detect anomalies
anomalies = detect_anomalies(df, stats_df)
anomalies_df = pd.DataFrame(anomalies)

# Save anomalies to a CSV file
anomalies_df.to_csv('anomalies_report.csv', index=False)

# Summary statistics
summary = anomalies_df.groupby('category').size().reset_index(name='anomaly_count')
print(summary)
