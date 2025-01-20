from dotenv import load_dotenv
import os

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

# Caminho dinâmico para o arquivo de credenciais
GCP_SERVICE_ACCOUNT = os.getenv(
    "GCP_SERVICE_ACCOUNT",
    os.path.join(BASE_DIR, "access-files", "SA-marcio_costa.json")
)

# Caminho dinâmico para as queries
QUERIES_PATH = os.getenv(
    "QUERIES_PATH",
    os.path.join(BASE_DIR, "src", "transformations", "queries")
)

BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
ICC_URL = os.getenv("ICC_URL")
ICF_URL = os.getenv("ICF_URL")