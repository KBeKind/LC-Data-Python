
from sqlalchemy import create_engine
import pandas as pd

username = 'launchcode-data'
password = 'lcd'
host = 'localhost'  # often 'localhost'
port = '3306'  # default MySQL port is 3306
database = 'launchcode-data'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')


csv_files = {
    'data-to-import/other-Lyft_B02510.csv': 'other_Lyft',

}


for csv_path, table_name in csv_files.items():
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')  # use 'append' to add to an existing table