from prefect.blocks.system import Secret

def get_azure_connection() -> str:
    """Carrega a connection string do Azure SQL a partir do Prefect Secret."""
    secret_block = Secret.load("dw-azsql-url", _sync=True)
    return secret_block.get()

def get_postgres_connection() -> str:
    """Carrega a connection string do PostgreSQL/Citus a partir do Prefect Secret."""
    secret_block = Secret.load("dw-psql-url", _sync=True)
    return secret_block.get()