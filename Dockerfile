# Usar la imagen oficial de Python 3.11.3 con slim-buster para mejor compatibilidad
FROM python:3.11-slim-buster

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema que puedan ser necesarias (como para compilar algunas dependencias de Python)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar solo el archivo de dependencias primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar las dependencias (considera quitar --no-deps si tienes problemas)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Variables de entorno recomendadas para producción
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Exponer el puerto (esto es solo documentación, Railway maneja los puertos automáticamente)
EXPOSE 8000

# Comando para ejecutar la aplicación (considera usar --reload solo en desarrollo)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]