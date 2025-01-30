import re
import pandas as pd
from datetime import datetime
import logging

# Configuração do logger
def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

def normalize_column_names(df):
    """Renomeia e normaliza os nomes das colunas para atender aos requisitos das queries."""
    rename_map = {
        'ÍNDICES E SEGMENTAÇÕES': 'indice',
        'Variação (%)': 'variacao'
    }
    df = df.rename(columns=rename_map)
    df.columns = [
        re.sub(r'[^a-zA-Z0-9_]', '_', col).lower()  # Substitui caracteres especiais por "_"
        for col in df.columns
    ]
    return df

def process_and_combine_sheets(file_path):
    """Processa todas as abas do Excel, renomeando colunas e combinando em um único DataFrame."""
    try:
        # Lê todas as abas do arquivo Excel
        sheets = pd.read_excel(file_path, sheet_name=None)
        combined_df = pd.DataFrame()

        # Itera pelas abas e processa
        for sheet_name, df in sheets.items():
            # Renomeia e normaliza as colunas
            df = normalize_column_names(df)

            # Filtra apenas as colunas relevantes
            relevant_columns = ['indice', 'variacao']
            if not all(col in df.columns for col in relevant_columns):
                logger.warning(f"A aba '{sheet_name}' está faltando colunas relevantes e será ignorada.")
                continue

            df = df[[col for col in df.columns if col in relevant_columns]]

            # Adiciona ao DataFrame combinado
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        return combined_df
    except Exception as e:
        logger.error(f"Erro ao processar as abas do arquivo: {e}")
        raise

def convert_xlsx_to_csv(input_filepath, output_filepath):
    try:
        combined_df = process_and_combine_sheets(input_filepath)

        if combined_df.empty:
            logger.warning(f"Nenhum dado foi combinado no DataFrame. O arquivo CSV não será criado.")
            return

        # Filtra o DataFrame para remover linhas indesejadas
        combined_df = combined_df[combined_df['indice'].notna() & combined_df['indice'].str.strip() != '']
        combined_df = combined_df[pd.to_numeric(combined_df['variacao'], errors='coerce').notna()]

        combined_df['load_timestamp'] = datetime.utcnow().isoformat()
        combined_df.to_csv(output_filepath, index=False)
        
        logger.info(f"Arquivo convertido com sucesso: {output_filepath}")
        return output_filepath
    except Exception as e:
        logger.error(f"Erro ao converter o arquivo {input_filepath}: {e}")
        raise



# def convert_xlsx_to_csv(input_filepath, output_filepath):
#     """Converte um arquivo .xlsx para .csv e adiciona a coluna load_timestamp."""
#     try:
#         # Processa e combina as abas do Excel
#         combined_df = process_and_combine_sheets(input_filepath)

#         # Adiciona a coluna load_timestamp
#         combined_df['load_timestamp'] = datetime.utcnow().isoformat()
   
#         # Salva como CSV
#         combined_df.to_csv(output_filepath, index=False)
#         logger.info(f"Arquivo convertido com sucesso: {output_filepath}")
#         return output_filepath
#     except Exception as e:
#         logger.error(f"Erro ao converter o arquivo {input_filepath}: {e}")
#         raise
