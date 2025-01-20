from src.crawler.downloader import download_files
from src.crawler.loader import load_all
from src.transformations.transformations import run_transformations


def main():
    print("Iniciando processo...")

    print("Download de arquivos...")
    # Passo 1: Baixar os arquivos
    #download_files()
    # Passo 2: Carregar os dados no BigQuery
    load_all()
    print("Processo concluído com sucesso!")

    print("Executando transformações...")
    run_transformations()

if __name__ == "__main__":
    main()
