import re
import pandas as pd
from datetime import datetime

def normalize_column_names(df):
    """Normaliza os nomes das colunas removendo caracteres especiais e espaços."""
    df.columns = [
        re.sub(r'[^a-zA-Z0-9_]', '_', col).lower()  # Substitui caracteres especiais por "_"
        for col in df.columns
    ]
    return df

def convert_xlsx_to_csv(input_filepath, output_filepath):
    """Converte um arquivo .xlsx para .csv e adiciona a coluna load_timestamp."""
    try:
        # Lê o arquivo .xlsx
        df = pd.read_excel(input_filepath)

        # Normaliza os nomes das colunas
        df = normalize_column_names(df)

        # Adiciona a coluna load_timestamp
        df['load_timestamp'] = datetime.utcnow().isoformat()

        # Salva como .csv
        df.to_csv(output_filepath, index=False)
        print(f"Arquivo convertido para CSV: {output_filepath}")
        return output_filepath
    except Exception as e:
        print(f"Erro ao converter {input_filepath} para CSV: {e}")
        raise
