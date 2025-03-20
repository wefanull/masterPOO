# Proyecto de Clima con Flask

Este proyecto es una aplicación web basada en Flask que consulta el clima de una ciudad utilizando la API de OpenWeather y genera imágenes dinámicas con formas geométricas que representan el estado del clima.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Docker**: [Instalar Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Incluido en Docker Desktop o puedes instalarlo por separado.

## Estructura del Proyecto desde la carpeta Flask
Flask

├──app

│ └── app.py

│ └── clima.py

│ └── dibuja.py

│ └── dibujarClima.py # Lógica para consultar el clima y generar imágenes

│ └── templates/

│ │ └──index.html

│ │ └── clima.html # Plantilla HTML para la interfaz de usuario

│ └── fonts

│ │ └── WinkySans.ttf

│ └── requirements.txt # Dependencias de Python

│ └── Dockerfile # Configuración para construir la imagen de Docker

└── docker-compose.yml # Configuración para iniciar el contenedor con Docker Compose


## Construir y Ejecutar con Docker Compose :
Asegúrate de que Docker y Docker Compose estén instalados.
Ejecuta el siguiente comando para construir la imagen y levantar el contenedor desde la carpeta de flask

docker compose up --build

## Acceder a la Aplicación :
Una vez que el servidor esté en funcionamiento, abre tu navegador y visita:

http://localhost:8000/clima

