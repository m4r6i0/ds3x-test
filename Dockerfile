# Use a imagem base com Python e Chromedriver
FROM joyzoursky/python-chromedriver:latest

# Definir o diretório de trabalho
WORKDIR /app

# Copiar as dependências para o container
COPY requirements.txt /app/

# Instalar as dependências do Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o container
COPY . /app/

# Definir variáveis de ambiente para o Chromedriver e o Chrome
ENV CHROME_BIN=/usr/bin/google-chrome
ENV CHROME_DRIVER=/usr/local/bin/chromedriver

# Comando padrão para execução
CMD ["python", "main.py"]
