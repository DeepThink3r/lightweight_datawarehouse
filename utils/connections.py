from urllib.parse import urlparse
from prefect.blocks.system import Secret


def get_azure_connection() -> str:
    """Carrega a connection string do Azure SQL a partir do Prefect Secret."""
    secret_block = Secret.load("dw-azsql-url", _sync=True)
    return secret_block.get()


def get_postgres_connection(as_conninfo: bool = True) -> str:

    secret_block = Secret.load("dw-psql-url", _sync=True)
    uri = secret_block.get()

    if not as_conninfo:
        return uri

    parsed = urlparse(uri)
    port = parsed.port or 5432
    dbname = parsed.path.lstrip("/")

    # Formata como pares chave=valor que a libpq aceita sem ambiguidades
    return (
        f"host={parsed.hostname} "
        f"port={port} "
        f"dbname={dbname} "
        f"user={parsed.username} "
        f"password={parsed.password}"
    )