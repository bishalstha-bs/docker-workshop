#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
from typing import Dict, Any


def run():

    # Postgres config
    pg_user = "root"
    pg_pass = "root"
    pg_host = "localhost"
    pg_port = 5433
    pg_db = "ny_taxi"

    # Dataset config
    year = 2021
    month = 1
    table_name = "yellow_taxi_data"
    chunksize = 100_000

    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"
    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"

    # Column types
    dtypes: Dict[str, Any] = {
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
        "congestion_surcharge": "float64",
    }

    parse_dates = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
    ]

    # DB engine
    engine = create_engine(
        f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )

    # CSV iterator
    df_iter = pd.read_csv(
        url,
        dtype=dtypes,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

    first = True

    for df_chunk in tqdm(df_iter, ascii=True):
        if first:
            df_chunk.head(0).to_sql(
                name=table_name,
                con=engine,
                if_exists="replace",
                index=False,
            )
            first = False

        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            method="multi",
        )


if __name__ == "__main__":
    run()
