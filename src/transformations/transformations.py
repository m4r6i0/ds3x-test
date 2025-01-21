from google.cloud import bigquery
from src.config.settings import GCP_SERVICE_ACCOUNT, QUERIES_PATH
from src.utils.utils import setup_logger
import os

logger = setup_logger()

def execute_queries_from_directory(directory_path):
    """Executa todas as queries em arquivos .sql de um diretório."""
    try:
        client = bigquery.Client.from_service_account_json(GCP_SERVICE_ACCOUNT)
        logger.info("config BigQuery Client")

        # Lista todos os arquivos .sql no diretório
        for filename in sorted(os.listdir(directory_path)):
            if filename.endswith(".sql"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, "r") as sql_file:
                    query = sql_file.read().strip()
                    if query:
                        logger.info(f"execute query file ... : {filename}")
                        client.query(query).result()  # Executa a query
                        logger.info("query send successfully")


    except Exception as e:
        logger.error(f"Error executed queries: {e}")


def run_transformations():
    """Executa as transformações SQL usando os arquivos da pasta de queries."""
    execute_queries_from_directory(QUERIES_PATH)
