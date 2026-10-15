import configparser
from pathlib import Path
from mssql_python import connect as mssql_connect
from psycopg2 import connect as pg_connect

def get_project_root() -> Path:
    """Retorna o diretório raiz do projeto."""
    return Path(__file__).resolve().parent.parent

def load_config(conf_filename: str = "pipeline.conf") -> configparser.ConfigParser:
    """Carrega o arquivo de configuração centralizado do pipeline."""
    base_dir = get_project_root()
    conf_path = base_dir / conf_filename
    
    parser = configparser.ConfigParser()
    if not conf_path.exists():
        raise FileNotFoundError(f"Arquivo de configuração não encontrado em: {conf_path}")
        
    parser.read(conf_path)
    return parser

def get_azure_connection(conf_filename: str = "pipeline.conf"):
    """Cria e retorna uma conexão ativa com o Azure SQL."""
    parser = load_config(conf_filename)
    
    hostname = parser.get("azsql_config", "hostname")
    username = parser.get("azsql_config", "username")
    password = parser.get("azsql_config", "password")
    dbname = parser.get("azsql_config", "database")
    
    connection_string = (
        f"Server={hostname};"
        f"Database={dbname};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=Yes;"   
    )
    return mssql_connect(connection_string)

def get_postgres_connection(conf_filename: str = "pipeline.conf"):
    """Cria e retorna uma conexão ativa com o PostgreSQL/Citus local."""
    parser = load_config(conf_filename)
    
    hostname = parser.get("psql_config", "hostname")
    username = parser.get("psql_config", "username")
    password = parser.get("psql_config", "password")
    dbname = parser.get("psql_config", "database")
    port = parser.get("psql_config", "port")
    
    pg_url = f"postgresql://{username}:{password}@{hostname}:{port}/{dbname}"
    return pg_connect(pg_url)