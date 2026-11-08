import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_postgres_connection
from adbc_driver_postgresql import dbapi

def transform_dim_products() -> None:

    uri_connection_pgsql = get_postgres_connection()

    tb_truncate = "TRUNCATE TABLE transformed.dim_products"

    tb_insert = """
        INSERT INTO transformed.dim_products (
            productid,
            productname,
            categoryname
        )
        select 
            p.productid,
            p.productname,
            c.categoryname
        from staging.products p
        left join staging.categories c
            ON p.categoryid = c.categoryid       
    """

    with dbapi.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:

            cur.execute(tb_truncate)
            cur.execute(tb_insert)

        conn.commit()

if __name__ == '__main__':
    transform_dim_products()