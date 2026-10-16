from prefect import flow, task
import papermill as pm


@task(name="1. executar staging.customers (Azure -> Postgres)", retries=1)
def task_staging_customers():
        pm.execute_notebook(
        input_path="tasks/ext_customers.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.employees (Azure -> Postgres)", retries=1)
def task_staging_employees():
        pm.execute_notebook(
        input_path="tasks/ext_employees.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.products (Azure -> Postgres)", retries=1)
def task_staging_products():
        pm.execute_notebook(
        input_path="tasks/ext_products.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.region (Azure -> Postgres)", retries=1)
def task_staging_region():
        pm.execute_notebook(
        input_path="tasks/ext_region.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.territories (Azure -> Postgres)", retries=1)
def task_staging_territories():
        pm.execute_notebook(
        input_path="tasks/ext_territories.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.employeeterritories (Azure -> Postgres)", retries=1)
def task_staging_employeeterritories():
        pm.execute_notebook(
        input_path="tasks/ext_employeeterritories.ipynb",
        output_path=None,
    )

@task(name="1. executar staging.shippers (Azure -> Postgres)", retries=1)
def task_staging_shippers():
        pm.execute_notebook(
        input_path="tasks/ext_shippers.ipynb",
        output_path=None,
    )

@flow(name="Pipeline staging", log_prints=True)
def pipeline_notebook_dw():

    task_staging_customers()
    task_staging_employees()
    task_staging_products()
    task_staging_region()
    task_staging_territories()
    task_staging_employeeterritories()
    task_staging_shippers()

if __name__ == "__main__":
    pipeline_notebook_dw()
