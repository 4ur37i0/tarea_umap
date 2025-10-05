# Usamos una versión de Python moderna
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos los requerimientos
COPY requirements.txt .

# Instalamos las librerías modernas
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de archivos ( .csv y script .py)
COPY . .

# Comando para ejecutar el script (cambiar nombre si es necesario)
CMD ["python", "main.py"]