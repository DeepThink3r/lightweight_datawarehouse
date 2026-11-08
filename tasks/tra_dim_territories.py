import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_postgres_connection
from adbc_driver_postgresql import dbapi

def transform_dim_territories() -> None:

    uri_connection_pgsql = get_postgres_connection()

    tb_truncate = "TRUNCATE TABLE transformed.dim_territories;"

    tb_insert = """
        INSERT INTO transformed.dim_territories (
            employeeid,
            territoryid,
            territorydescription,
            regiondescription
        )
        SELECT
            et.employeeid,
            et.territoryid,
            t.territorydescription,
            r.regiondescription 
        FROM staging.employeeterritories et
        LEFT join staging.territories t 
            on et.territoryid = t.territoryid
        LEFT join staging.region r
            ON t.regionid = r.regionid 
    """

    with dbapi.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:

            cur.execute(tb_truncate)
            cur.execute(tb_insert)

        conn.commit()

if __name__ == '__main__':
    transform_dim_territories()