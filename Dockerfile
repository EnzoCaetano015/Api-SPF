# Etapa 1: Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# Etapa 2: Define o diretório de trabalho dentro do container
WORKDIR /app

# Etapa 3: Copia os arquivos da aplicação para o diretório de trabalho
COPY . .

# Etapa 4: Instala as dependências
RUN pip install --no-cache-dir fastapi uvicorn python-dotenv mysql-connector-python

# Etapa 5: Expõe a porta usada pelo uvicorn
EXPOSE 8000

# Etapa 6: Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
