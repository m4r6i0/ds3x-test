# Dockerfile

FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    libnss3 \
    libgconf-2-4 \
    fonts-liberation \
    libgbm1 \
    libvulkan1 \
    xdg-utils \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Criar ambiente virtual
RUN python3 -m venv /app/venv

# Ativar o ambiente virtual e instalar dependências
COPY requirements.txt /app/
RUN /app/venv/bin/pip install --upgrade pip && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Adicionar o ambiente virtual ao PATH
ENV PATH="/app/venv/bin:$PATH"
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Comando padrão
CMD ["python", "main.py"]
