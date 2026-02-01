#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm


import sys
print(sys.executable)



df = pd.read_csv(url)


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)

prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')


df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

def run():
    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port =  5433
    pg_db   = 'ny_taxi'


    year = 2021
    month = 1
    chunksize=100000

    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

df.head()



get_ipython().system('uv add sqlalchemy')



get_ipython().system('uv add psycopg2-binary')




print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))



df.to_sql(name='yellow_taxi_data', con=engine)




df.head(0)








len(df)







df_iter







# In[18]:


for df_chunk in tqdm(df_iter, ascii=True):
    df_chunk.to_sql(
        name="yellow_taxi_data",
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )


# In[ ]:


import sys
sys.executable


# In[ ]:




