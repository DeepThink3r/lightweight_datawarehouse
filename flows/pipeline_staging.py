from prefect import flow, task
from prefect_github import GitHubRepository
import papermill as pm

@task(retries=1, log_prints=True)
def run_notebook_task(table_name: str, notebook_path: str):
    print(f"Iniciando extração para: {table_name}...")
    pm.execute_notebook(
        input_path=notebook_path,
        output_path=None,
    )
    print(f"Finalizado com sucesso: {table_name}!")



@flow(name="Pipeline staging", log_prints=True)
def pipeline_notebook_dw():

    t_customers = run_notebook_task.submit("staging.customers", "tasks/ext_customers.ipynb")
    t_employees = run_notebook_task.submit("staging.employees", "tasks/ext_employees.ipynb")
    t_products = run_notebook_task.submit("staging.products", "tasks/ext_products.ipynb")
    t_region = run_notebook_task.submit("staging.region", "tasks/ext_region.ipynb")
    t_shippers = run_notebook_task.submit("staging.shippers", "tasks/ext_shippers.ipynb")
    t_categories = run_notebook_task.submit("staging.categories", "tasks/ext_categories.ipynb")
    t_territories = run_notebook_task.submit("staging.territories", "tasks/ext_territories.ipynb")
    t_employeeterritories = run_notebook_task.submit("staging.employeeterritories", "tasks/ext_employeeterritories.ipynb")
    t_orders = run_notebook_task.submit("staging.orders", "tasks/ext_orders.ipynb")
    t_order_details = run_notebook_task.submit("staging.order_details", "tasks/ext_order_details.ipynb")

if __name__ == "__main__":

    pipeline_notebook_dw.deploy(
        name="deploy-staging-github",
        work_pool_name="default-docker-pool",       
    
    
        github_storage = GitHubRepository(
            repository="https://github.com/DeepThink3r/lightweight_datawarehouse.git",
            reference="dev"
            ),

        job_variables={
            "env": {
                "EXTRA_PIP_PACKAGES": "-r requirements.txt"
            }
        }
    )
    print("Deploy do pipeline de staging registrado com sucesso no Prefect Server!")       
    