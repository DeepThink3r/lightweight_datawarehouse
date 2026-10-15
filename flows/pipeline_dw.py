from prefect import flow, task
import papermill as pm
import tempfile

@task(name="1. executar staging (Azure -> Postgres)", retries=1)
def task_staging():
        pm.execute_notebook(
        input_path="tasks/ext_cliente.ipynb",
        output_path=None,  # Salva no lixo/temporário do sistema
    )

@flow(name="Pipeline DW", log_prints=True)
def pipeline_notebook_dw():

    task_staging()

if __name__ == "__main__":
    pipeline_notebook_dw()