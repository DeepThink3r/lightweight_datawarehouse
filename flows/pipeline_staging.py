from pathlib import Path

import papermill as pm
from prefect import flow, task
from prefect.task_runners import ThreadPoolTaskRunner

BASE_DIR = Path(__file__).resolve().parent.parent

TABELAS = [
    "customers",
    "employees",
    "products",
    "region",
    "territories",
    "employeeterritories",
    "shippers",
    "categories",
    "orders",
    "order_details",
]


@task(retries=1)
def task_staging(tabela: str):
    pm.execute_notebook(
        input_path=str(BASE_DIR / "tasks" / f"ext_{tabela}.ipynb"),
        output_path=None,
    )


@flow(name="Pipeline staging", task_runner=ThreadPoolTaskRunner(max_workers=2))
def pipeline_notebook_dw():
    futures = [task_staging.submit(t) for t in TABELAS]
    for f in futures:
        f.result()

if __name__ == "__main__":
     pipeline_notebook_dw.serve(
        name="dw-diario",
        cron="0 6 * * *",
    )
