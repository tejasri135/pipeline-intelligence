import duckdb
csv_file_path = 'sample_data.csv'
query = f"""
    SELECT 
    status,count(1) as status_count from read_csv_auto('{csv_file_path}') group by status;
    """
# Execute the query and fetch the results as a Pandas DataFrame
df_result = duckdb.sql(query).df()

# Display the query output
print(df_result)

query1 = f"""
    SELECT 
    status,count(1) as status_count from read_csv_auto('{csv_file_path}') 
    where status = 'failed' group by status;
    """
# Execute the query and fetch the results as a Pandas DataFrame
df_result1 = duckdb.sql(query1).df()
print(df_result1)
