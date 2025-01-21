from src.utils.data_utils import convert_xlsx_to_csv
from google.cloud import bigquery
from src.config.settings import GCP_SERVICE_ACCOUNT, BIGQUERY_DATASET
from src.utils.utils import setup_logger

logger = setup_logger()

def load_to_bigquery(filepath, table_name):
    """Carrega um arquivo CSV no BigQuery."""
    try:
        client = bigquery.Client.from_service_account_json(GCP_SERVICE_ACCOUNT)
        table_id = f"{BIGQUERY_DATASET}.{table_name}"

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            autodetect=True
        )

        with open(filepath, "rb") as file:
            job = client.load_table_from_file(file, table_id, job_config=job_config)
        job.result()  # Aguarda a conclusão do job

        logger.info(f"Table {table_name} successfully loaded into BigQuery")
    except Exception as e:
        logger.error(f"Error loading table ...: {table_name} ... : {e}")

def load_all():
    """Processa e carrega todos os arquivos no BigQuery."""
    try:
        # Caminhos dos arquivos originais e temporários
        icc_xlsx = "data/icc.xlsx"
        icc_csv = "data/icc.csv"
        icf_xlsx = "data/icf.xlsx"
        icf_csv = "data/icf.csv"

        # Converte os arquivos .xlsx para .csv
        convert_xlsx_to_csv(icc_xlsx, icc_csv)
        convert_xlsx_to_csv(icf_xlsx, icf_csv)

        # Carrega os arquivos convertidos no BigQuery
        load_to_bigquery(icc_csv, "icc_raw")
        load_to_bigquery(icf_csv, "icf_raw")

    except Exception as e:
        logger.error(f"Error processing files ... : {e}")
