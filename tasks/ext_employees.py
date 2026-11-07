import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_azure_connection, get_postgres_connection
from adbc_driver_postgresql import dbapi

def extract_employees() -> None:

    uri_connection_azsql = get_azure_connection()
    uri_connection_pgsql = get_postgres_connection()


    ext_query="""
                SELECT 
                    EmployeeID,
                    LastNameI,
                    FirstNameI,
                    TitleI,
                    TitleOfCourtesyI,
                    BirthDateI,
                    HireDateI,
                    AddressI,
                    CityI,
                    RegionI,
                    PostalCodeI,
                    CountryI,
                    HomePhoneI,
                    ExtensionI,
                    NotesI,
                    ReportsToI,
                    PhotoPathI,
                    'dbo.nowrthwind' as origem
                FROM employees a;
                """


    df = pl.read_database_uri(query=ext_query,uri=uri_connection_azsql,engine="connectorx")


    df = df.rename({col: col.lower() for col in df.columns})

    # 2. Converte tudo para string para caber nas colunas VARCHAR do staging
    df = df.cast(pl.String)

    # 3. Truncate e carga direta via ADBC DBAPI
    with dbapi.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:
            cur.execute("TRUNCATE TABLE staging.employees;")
        conn.commit()

        df.write_database(
            table_name='staging.employees',
            connection=conn,
            engine="adbc",
            if_table_exists="append"
        )


if __name__ == "__main__":
    extract_employees()