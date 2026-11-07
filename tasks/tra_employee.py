import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_azure_connection, get_postgres_connection
from adbc_driver_postgresql import dbapi

def transform_employee() -> None:

    uri_connection_pgsql = get_postgres_connection()

    tb_truncate = "TRUNCATE TABLE transformed.dim_employee;"

    tb_insert = """
        INSERT INTO transformed.dim_employee (
            employeeid,
            name,
            title
        )
        SELECT
            employeeid,
            firstname ||' ' || lastname) as name,
            title
        FROM staging.employees
    """

    with dbapi.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:

            cur.execute(tb_truncate)

            cur.execute(tb_insert)

        conn.commit()

if __name__ == '__main__':
    transform_employee()