from sqlalchemy import create_engine
import pandas as pd
import os

username = 'launchcode-data'
password = 'lcd'
host = 'localhost'
port = '3306'
database = 'assignment_three'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

csv_files = {
    'all.data.combined.csv': 'alldata',
    'ce.datatype.csv': 'datatype',
    'ce.footnote.csv': 'footnote',
    'ce.industry.csv': 'industry',
    'ce.period.csv': 'period',
    'ce.seasonal.csv': 'seasonal',
    'ce.series.csv': 'series',
    'ce.supersector.csv': 'supersector',
}

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Function to read and insert CSV data in chunks with stripped column names
def insert_csv_in_chunks(csv_path, table_name, chunk_size=10000):
    if os.path.isfile(csv_path):
        for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
            chunk.columns = chunk.columns.str.strip()  # Strip whitespace from column names
            chunk.to_sql(table_name, con=engine, index=False, if_exists='append')
        print(f"Successfully imported {csv_path} into {table_name}")
    else:
        print(f"File {csv_path} not found.")

for csv_path, table_name in csv_files.items():
    insert_csv_in_chunks(csv_path, table_name)
