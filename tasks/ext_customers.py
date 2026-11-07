import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_azure_connection, get_postgres_connection


def extract_customers() -> None:
    uri_connection_azsql = get_azure_connection()
    uri_connection_pgsql = get_postgres_connection()


    ext_query = """
                SELECT 
                    a.*,
                    'dbo.nowrthwind' as origem,
                    current_timestamp as ext_timestmp
                FROM Customers a;
                """


    df = pl.read_database_uri(
        query=ext_query,
        uri=uri_connection_azsql,
        engine="connectorx"
        )


    df.write_database(
        table_name='staging.customers',
        connection=uri_connection_pgsql,
        engine="adbc",
        if_table_exists="append"
    )

if '__name__' == '__main__':
    extract_customers()
