import pandas as pd
file_name = 'sample_data.csv'
df = pd.read_csv(file_name)
df['error_rate'] =(df['errors'] / df['records']) *100
print(df[df['error_rate'] > 3])
print(df['partner'].value_counts())
print(df.groupby('partner')['records'].sum())