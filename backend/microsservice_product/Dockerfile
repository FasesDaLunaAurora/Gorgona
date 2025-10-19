FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Evita mensagens de buffer no output (útil para logs)
ENV PYTHONUNBUFFERED=1

# Copia apenas o requirements.txt primeiro (para cache eficiente)
COPY requirements.txt .

# Instala dependências do sistema e pacotes Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código 
COPY ./src ./src

# Expõe a porta usada pelo FastAPI (Uvicorn)
EXPOSE 8000

# ---- Comando padrão para iniciar o app ----
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]