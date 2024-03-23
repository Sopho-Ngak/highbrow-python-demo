import os

import pandas as pd
from IPython import embed
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# base = os.path.join(os.path.dirname(__file__))


# print(base)

# load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


# accounts_user
engine = create_engine(f"postgresql+psycopg2://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DBT_NAME']}")
conn = engine.connect()


# df_csv = pd.read_csv('data.csv')

print("Readng json file")
df_json = pd.read_json('data.json')
print("Done")

print("====================Reading from database=================")

# df_from_db = pd.read_sql('select * from accounts_user;', con=conn)

print("Converting into csv")
# df_from_db.to_csv('data_from_db_2.csv', index=False)
print("____________Done________________")


print("Start loading data into our database")
df_json.to_sql('python_demo', schema='demo', con=conn, index=False, if_exists='append')
print('______________data loadded_______________________')

# embed()



# print(df_csv)
# print(df_json)