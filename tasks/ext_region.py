import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_azure_connection, get_postgres_connection


def extract_region() -> None:
    uri_connection_azsql = get_azure_connection()
    uri_connection_pgsql = get_postgres_connection()


    ext_query="""
                SELECT 
                    a.*,
                    'dbo.nowrthwind' as origem,
                    current_timestamp as ext_timestmp
                FROM region a;
                """


    df = pl.read_database_uri(query=ext_query,uri=uri_connection_azsql,engine="connectorx")


    df.write_database(
        table_name='staging.region',
        connection=uri_connection_pgsql,
        engine="adbc",
        if_table_exists="replace"
    )

if '__name__' == '__main__':
    extract_region()
