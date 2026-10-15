from prefect import flow, task
import papermill as pm
import tempfile

@task(name="1. executar staging (Azure -> Postgres)", retries=1)
def task_staging():
    with tempfile.NamedTemporaryFile(suffix=".ipynb", delete=False) as temp:
        output_path = temp.name

        pm.execute_notebook(
        input_path="tasks/tst.extracao.ipynb",
        output_path=output_path,  # Salva no lixo/temporário do sistema
    )

@flow(name="Pipeline DW", log_prints=True)
def pipeline_notebook_dw():

    task_staging()

if __name__ == "__main__":
    pipeline_notebook_dw()