import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto (lightweight_datawarehouse) ao sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from prefect import flow, task
from prefect.runner.storage import GitRepository

# Rotinas
from tasks.ext_categories import extract_categories
from tasks.ext_customers import extract_customers
from tasks.ext_employees import extract_employees
from tasks.ext_products import extract_products
from tasks.ext_region import extract_region
from tasks.ext_shippers import extract_shippers
from tasks.ext_territories import extract_territories
from tasks.ext_employeeterritories import extract_employeeterritories
from tasks.ext_orders import extract_orders
from tasks.ext_order_details import extract_order_details

# Tasks Staging

@task(name="staging.customers", retries=2, retry_delay_seconds=10, log_prints=True)
def task_customers():
    extract_customers()

@task(name="staging.employees", retries=2, retry_delay_seconds=10, log_prints=True)
def task_employees():
    extract_employees()

@task(name="staging.products", retries=2, retry_delay_seconds=10, log_prints=True)
def task_products():
    extract_products()

@task(name="staging.region", retries=2, retry_delay_seconds=10, log_prints=True)
def task_region():
    extract_region()

@task(name="staging.shippers", retries=2, retry_delay_seconds=10, log_prints=True)
def task_shippers():
    extract_shippers()

@task(name="staging.categories", retries=2, retry_delay_seconds=10, log_prints=True)
def task_categories():
    extract_categories()

@task(name="staging.territories", retries=2, retry_delay_seconds=10, log_prints=True)
def task_territories():
    extract_territories()

@task(name="staging.employeeterritories", retries=2, retry_delay_seconds=10, log_prints=True)
def task_employeeterritories():
    extract_employeeterritories()

@task(name="staging.orders", retries=2, retry_delay_seconds=10, log_prints=True)
def task_orders():
    extract_orders()

@task(name="staging.order_details", retries=2, retry_delay_seconds=10, log_prints=True)
def task_order_details():
    extract_order_details()

@flow(name="Pipeline staging", log_prints=True)
def pipeline_notebook_dw():

    t_cust = task_customers.submit()
    t_emp = task_employees.submit()
    t_prod = task_products.submit()
    t_reg = task_region.submit()
    t_ship = task_shippers.submit()
    t_cat = task_categories.submit()
    t_terr = task_territories.submit()
    t_emp_terr = task_employeeterritories.submit()
    t_ord = task_orders.submit()
    t_det = task_order_details.submit()

if __name__ == "__main__":
    pipeline_notebook_dw()