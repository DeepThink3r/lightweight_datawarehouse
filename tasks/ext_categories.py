import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_azure_connection, get_postgres_connection
import psycopg2

def extract_categories() -> None:

    uri_connection_azsql = get_azure_connection()
    uri_connection_pgsql = get_postgres_connection()


    ext_query = """SELECT 
                    CategoryID,
                    CategoryName,
                    Description,
                    Picture,
                    'dbo.nowrthwind' AS origem,
                    current_timestamp AS ext_timestmp
                FROM categories
                """


    df = pl.read_database_uri(query=ext_query, 
                            uri=uri_connection_azsql, 
                            engine="connectorx")


    df = df.rename({col: col.lower() for col in df.columns})


    #Limpa a tabela
    with psycopg2.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE staging.categories")
        conn.commit()

    # Carrega os dados
        df.write_database(
            table_name='staging.categories',
            connection=conn,
            engine='adbc',
            if_table_exists="append"
        )

if __name__ == "__main__":
    extract_categories()
