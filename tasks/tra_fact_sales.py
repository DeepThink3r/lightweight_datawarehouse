import sys
from pathlib import Path

root_dir = Path.cwd().parent 
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

import polars as pl
from utils.connections import get_postgres_connection
from adbc_driver_postgresql import dbapi

def transform_fact_sales() -> None:

    uri_connection_pgsql = get_postgres_connection()

    tb_truncate = "TRUNCATE TABLE transformed.fact_sales"

    tb_insert = """
        INSERT INTO transformed.fact_sales (
            orderid,
            customerid,
            salesmanid,
            orderdate,
            requireddate,
            shippeddate,
            freight,
            shipname,
            leadtime,
            overdueorders,
            productid,
            unitprice,
            discount,
            unitpricediscount
        )
        with convert_type as (
            select
                o.orderid,
                o.customerid,
                o.employeeid as salesmanid,
                CAST(o.orderdate AS DATE) as orderdate,
                CAST(o.requireddate AS DATE) as requireddate,
                CAST(o.shippeddate AS DATE) as shippeddate,
                CAST(o.freight AS DECIMAL) as freight,
                shipname,
                od.productid,
                CAST(od.unitprice AS DECIMAL) as unitprice,
                CAST(od.quantity AS DECIMAL) as quantity,
                CAST(od.discount AS DECIMAL) as discount
            from staging.orders o
            inner join staging.order_details od 
                on o.orderid = od.orderid
        ), calculated as (
            select
                orderid,
                customerid,
                salesmanid,
                orderdate,
                requireddate,
                shippeddate,
                freight,
                shipname,
                CASE
                    WHEN shippeddate IS NOT NULL THEN (shippeddate - orderdate)
                    ELSE 0
                END AS leadtime,
                CASE
                    WHEN shippeddate > requireddate THEN 1
                    ELSE 0
                END overdueorders,	
                productid,
                unitprice,
                discount,
                (unitprice * (1 - discount)) as unitpricediscount
            from convert_type 
        )
        select * from calculated
    """

    with dbapi.connect(uri_connection_pgsql) as conn:
        with conn.cursor() as cur:

            cur.execute(tb_truncate)
            cur.execute(tb_insert)

        conn.commit()

if __name__ == '__main__':
    transform_fact_sales()