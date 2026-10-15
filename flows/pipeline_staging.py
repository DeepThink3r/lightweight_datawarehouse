from prefect import flow, task
import papermill as pm
import tempfile

@task(name="1. executar staging.customers (Azure -> Postgres)", retries=1)
def task_staging_customers():
        pm.execute_notebook(
        input_path="tasks/ext_customers.ipynb",
        output_path=None,  # Salva no lixo/temporário do sistema
    )

@task(name="1. executar staging.employees (Azure -> Postgres)", retries=1)
def task_staging_employees():
        pm.execute_notebook(
        input_path="tasks/ext_employees.ipynb",
        output_path=None,  # Salva no lixo/temporário do sistema
    )

@flow(name="Pipeline DW", log_prints=True)
def pipeline_notebook_dw():

    task_staging_customers()
    task_staging_employees()

if __name__ == "__main__":
    pipeline_notebook_dw()
