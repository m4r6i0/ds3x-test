import datetime

from src.crawler.downloader import download_files
from src.crawler.loader import load_all
from src.transformations.transformations import run_transformations
from src.utils.utils import setup_logger

logger = setup_logger()
def main():

    now = datetime.datetime.now()

    logger.info(f"Starting Process at ... : {now}")

    logger.info("Step 1 Download Files...")
    download_files()

    logger.info("Step 2 Load data in Big Query")
    load_all()

    logger.info("Step 3 Data Transformations")
    run_transformations()

    logger.info(f"Finished Process ... : {now}")

if __name__ == "__main__":
    main()
