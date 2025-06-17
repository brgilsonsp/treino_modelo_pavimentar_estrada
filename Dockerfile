# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Instalar dependências de sistema para bibliotecas geoespaciais
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Instalar as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN --mount=type=cache,target=/root/.cache/pip pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação e os dados
COPY . .

#Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "start.py"]
