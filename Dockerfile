#imagen base de Python
FROM python:3.13.0

#directorio de trabajo
WORKDIR /app

# Copiar los archivos de código
RUN pip install flask
COPY microservice.py microservice.py 

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "microservice.py"]

