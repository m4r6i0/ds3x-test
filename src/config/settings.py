from dotenv import load_dotenv
import os
from src.utils.utils import setup_logger

logger = setup_logger()

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

# Caminho dinâmico para as queries
default_queries_path = os.path.join(BASE_DIR, "transformations", "queries")
QUERIES_PATH = default_queries_path
if not os.path.dirname(QUERIES_PATH):
    logger.warn(f"Default queries path not found ... : {QUERIES_PATH}")

# Caminho padrão para o arquivo de credenciais
GCP_SERVICE_ACCOUNT = os.getenv("GCP_SERVICE_ACCOUNT")
if not os.path.isfile(GCP_SERVICE_ACCOUNT):
    logger.error(f"GCP_SERVICE_ACCOUNT not found ... : {GCP_SERVICE_ACCOUNT}")
    raise FileNotFoundError(f"Credential CGP file not found ... : {GCP_SERVICE_ACCOUNT}")

BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
ICC_URL = os.getenv("ICC_URL")
ICF_URL = os.getenv("ICF_URL")