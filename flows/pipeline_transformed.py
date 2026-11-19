import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto (lightweight_datawarehouse) ao sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from prefect import flow, task

from lightweight_datawarehouse.tasks.int_salesman_cleansed import transform_dim_salesman
from lightweight_datawarehouse.tasks.int_territories_cleansed import transform_dim_territories
from lightweight_datawarehouse.tasks.int_customers_cleansed import transform_dim_customers
from lightweight_datawarehouse.tasks.int_products_cleansed import transform_dim_products
from lightweight_datawarehouse.tasks.int_salesorder_merged import transform_fact_sales


@task(name='transformed.dim_salesman', retries=2, retry_delay_seconds=10, log_prints=True)
def task_dim_salesman():
    transform_dim_salesman()

@task(name='transformed.dim_territories', retries=2, retry_delay_seconds=10, log_prints=True)
def task_dim_territories():
    transform_dim_territories()

@task(name='transformed.dim_customers', retries=2, retry_delay_seconds=10, log_prints=True)
def task_dim_customers():
    transform_dim_customers()

@task(name='transformed.dim_products', retries=2, retry_delay_seconds=10, log_prints=True)
def task_dim_produtcs():
    transform_dim_products()

@task(name='transformed.fact_sales', retries=2, retry_delay_seconds=10, log_prints=True)
def task_fact_sales():
    transform_fact_sales()


@flow(name='Pipeline transform', log_prints=True)
def pipeline_notebook_transform():

    t_dim_salesman = task_dim_salesman.submit()
    t_dim__territories = task_dim_territories.submit()
    t_dim_customers = task_dim_customers.submit()
    t_dim_products = task_dim_produtcs.submit()
    t_fact_sales = task_fact_sales.submit()

    features = [
        t_dim_salesman,
        t_dim__territories,
        t_dim_customers,
        t_dim_products,
        t_fact_sales
    ]

    for feature in features:
        feature.result()

if __name__ == "__main__":
    pipeline_notebook_transform()