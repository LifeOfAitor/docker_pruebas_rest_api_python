# Imagen base con Python y pip
FROM python:3.11-alpine

# Instalamos dependencias necesarias para compilar e instalar
RUN apk add --no-cache gcc musl-dev libffi-dev

# Directorio de trabajo
WORKDIR /app

# Copiar los requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar tu archivo main.py
COPY main.py .

# Exponer puerto
EXPOSE 8000
EXPOSE 5000

# Ejecutar FastAPI con uvicorn
CMD ["uvicorn", "main:app",  "--port", "8000"]
#CMD ["python", "main.py"]
