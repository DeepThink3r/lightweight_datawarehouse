import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto (lightweight_datawarehouse) ao sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from prefect import flow, task

from tasks.tra_employee import transform_employee


@task(name='transformed.employee', retries=2, retry_delay_seconds=10, log_prints=True)
def task_dim_employee():
    transform_employee()

@flow(name='Pipeline transform', log_prints=True)
def pipeline_notebook_transform():

    t_dim_emp = task_dim_employee.submit()

if '_name__' == "__main__":
    pipeline_notebook_transform()