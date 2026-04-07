# 📸 InstaReels
Este proyecto es una herramienta construida con **Python (Flask)** y **yt-dlp** para la extracción y descarga de Reels de Instagram. El objetivo principal es demostrar las técnicas de **optimización de imágenes Docker**, comparando diferentes métodos de construcción para reducir el peso.


## 🛠️ Guía de Uso (Docker)

### 1. Clonar el proyecto
```bash
#Entrar a la terminal y clonar el repositorio
git clone https://github.com/Jmedrano-Git/InstaReels.git

#Entrar a la app
cd evaluacion_nube4

#Construir la imagen multistage
docker build -t app:multistage -f Dockerfile.multistage .

#Desplegar el contenedor
docker run -d -p 6969:6969 --name instareels app:multistage

# VERSION OPTIMIZADA
#Construir la imagen optimizada
docker build -t app:optimizada -f Dockerfile.optimizada .

#Desplegar el contenedor
docker run -d -p 6969:6969 --name instareels app:optimizada

# VERSION NORMAL
#Construir la imagen multistage
docker build -t app:normal -f Dockerfile.normal .

#Desplegar el contenedor
docker run -d -p 6969:6969 --name instareels app:normal

```
Abre tu navegador en: http://localhost:6969

## 📊 Resultados de la Evaluación 
Se realizaron pruebas con tres tipos de Dockerfiles para analizar la eficiencia en el despliegue de la nube:
<img width="893" height="58" alt="image" src="https://github.com/user-attachments/assets/82077521-9a1a-4873-a389-7a5cd474bdb8" />
