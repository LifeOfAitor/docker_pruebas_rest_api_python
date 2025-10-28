# Imagen base con Python y pip
FROM python:3.11-alpine

# Instalamos dependencias necesarias para compilar e instalar
RUN apk add --no-cache gcc musl-dev libffi-dev

# Directorio de trabajo
WORKDIR /app

# Copiar los requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY main.py .

# Exponer el puerto (FastAPI suele usar 8000)
EXPOSE 8000

# Crear usuario no root (opcional pero recomendado)
RUN adduser -D appuser
USER appuser

# Ejecutar FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#para que funcione:
    # docker build -t mirestapi:v1 .
    # docker run -d -p 8000:8000 --name restApi mirestapi:v1