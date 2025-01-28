from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
import os
import tempfile
from src.utils.utils import setup_logger
from src.config.settings import ICC_URL, ICF_URL
from webdriver_manager.chrome import ChromeDriverManager
import shutil


logger = setup_logger()

def setup_driver(download_dir):
    """Configura o WebDriver do Selenium automaticamente"""
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executa o navegador em modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument(f"--window-size=1920,1080")
    options.add_argument("--disable-setuid-sandbox")

    config_temp_downloads(download_dir, options)
    logger.info(f"configuration driver ... : {options}")

    return webdriver.Chrome(service=service, options=options)
    #return webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

def download_with_selenium(url, output_path):
    """Faz o download do arquivo usando Selenium para uma pasta temporária"""
    with tempfile.TemporaryDirectory() as temp_dir:  # Cria uma pasta temporária
        logger.info(f"Temp Directory ... : {temp_dir}")
        driver = setup_driver(temp_dir)
        try:
            logger.info(f"Read page: {url}")
            driver.get(url)

            # Localizar e clicar no botão "Download tabelas"
            download_button = driver.find_element(By.CLASS_NAME, "download")  # Usar a classe do botão
            ActionChains(driver).move_to_element(download_button).click().perform()

            # Aguarda o download completar (ajuste o tempo se necessário)
            time.sleep(10)

            # Identificar o arquivo baixado
            downloaded_files = os.listdir(temp_dir)
            if not downloaded_files:
                raise FileNotFoundError("file not found")

            logger.info(f"Downloaded files: {downloaded_files}")

            # Verificar se o arquivo já existe no destino e sobrescrever ou renomear
            if os.path.exists(output_path):
                os.remove(output_path)  # Remove o arquivo existente para evitar conflitos

            # Renomear o primeiro arquivo encontrado
            downloaded_file = os.path.join(temp_dir, downloaded_files[0])
            shutil.move(downloaded_file, output_path)
            logger.info(f"Saved file in {output_path}")

        except Exception as e:
            logger.error(f"Failed downloaded files ... : {e}")
        finally:
            driver.quit()


def config_temp_downloads(download_dir, options):
    # Configuração do diretório de downloads
    prefs = {
        "download.default_directory": download_dir,  # Define o diretório de download
        "download.prompt_for_download": False,  # Desabilita prompts de download
        "download.directory_upgrade": True,  # Permite atualizações automáticas no diretório
        "safebrowsing.enabled": True  # Evita bloqueios de segurança
    }
    options.add_experimental_option("prefs", prefs)

def download_files():
    """Faz o download dos arquivos ICC e ICF"""

    # Verifica se a pasta 'data' existe e remove, caso positivo
    if os.path.exists("data"):
        logger.info("Pasta 'data' encontrada. Removendo...")
        shutil.rmtree("data")
        logger.info("Pasta 'data' removida com sucesso.")

    os.makedirs("data", exist_ok=True)

    logger.info("Downloading ICC")
    download_with_selenium(ICC_URL, "data/icc.xlsx")
    logger.info("Downloading ICF")
    download_with_selenium(ICF_URL, "data/icf.xlsx")