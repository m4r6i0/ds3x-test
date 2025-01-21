# Dockerfile

# Usar uma imagem base mais recente do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de dependências para o contêiner
COPY requirements.txt /app/

# Atualizar o pip antes de instalar as dependências
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto para o contêiner
COPY . /app/

# Definir o comando padrão ao iniciar o contêiner
CMD ["python", "main.py"]
