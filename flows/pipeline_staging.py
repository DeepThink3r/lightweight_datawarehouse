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

# Tasks
@task(name="staging.categories", retries=2, retry_delay_seconds=10, log_prints=True)
def task_categories():
    extract_categories()

@flow(name="Pipeline staging", log_prints=True)
def pipeline_notebook_dw():

    t_cat = task_categories.submit()

if __name__ == "__main__":
    pipeline_notebook_dw()