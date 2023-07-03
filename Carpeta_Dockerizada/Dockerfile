# Establecer la imagen base
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos .py al directorio de trabajo en el contenedor
COPY ./MSG/*.py ./

# Instalar las dependencias necesarias
# RUN pip install --no-cache-dir <lista de dependencias>
# LABEL description="Carpeta"


# Establecer el comando de inicio para el contenedor
CMD [ "python", "launcher.py" ]
