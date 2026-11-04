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

    source_repo = GitRepository(
        url="https://github.com/DeepThink3r/lightweight_datawarehouse.git",
        branch="dev"
    )

    pipeline_notebook_dw.from_source(
        source=source_repo,
        entrypoint="flows/pipeline_staging.py:pipeline_notebook_dw"
    ).deploy(
        name="deploy-staging-github",
        work_pool_name="default-docker-pool",
        parameters={},
        job_variables={
            "env": {
                "PREFECT_API_URL": "http://192.168.86.138:4200/api"
            }
        }
    )
    print("Deploy do pipeline de staging (branch dev) registado com sucesso no Prefect Server!")