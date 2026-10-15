from prefect import flow, task
import papermill as pm
import tempfile

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

@flow(name="Pipeline staging", log_prints=True)
def pipeline_notebook_dw():

    task_staging_customers()
    task_staging_employees()
    task_staging_products()

if __name__ == "__main__":
    pipeline_notebook_dw()
