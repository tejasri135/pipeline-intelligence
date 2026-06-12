import pandas
csv_file_path = 'sample_data.csv'
# Read the CSV file into a Pandas DataFrame
df = pandas.read_csv(csv_file_path)
status_counts =df['status'].value_counts()
print(status_counts)
failed_csv = df[df['status'] == 'failed']
print(failed_csv)
