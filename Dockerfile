# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el contenido del proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir flask

# Expone el puerto
EXPOSE 5000

# Comando por defecto para correr la app
CMD ["python", "app.py"]
