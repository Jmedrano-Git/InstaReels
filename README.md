# 📸 InstaReels
Este proyecto es una herramienta construida con **Python (Flask)** y **yt-dlp** para la extracción y descarga de Reels de Instagram. El objetivo principal es demostrar las técnicas de **optimización de imágenes Docker**, comparando diferentes métodos de construcción para reducir el peso.


## 🛠️ Guía de Uso (Docker)

### 1. Clonar el proyecto
```bash
git clone <TU_URL_DE_GITHUB>
cd evaluacion_nube4

#Construir la imagen multistage
docker build -t app:multistage -f Dockerfile.multistage .

#Desplegar el contenedor
docker run -d -p 6969:6969 --name instareels app:multistage
```
Abre tu navegador en: http://localhost:6969

## 📊 Resultados de la Evaluación 
Se realizaron pruebas con tres tipos de Dockerfiles para analizar la eficiencia en el despliegue de la nube:
<img width="893" height="58" alt="image" src="https://github.com/user-attachments/assets/82077521-9a1a-4873-a389-7a5cd474bdb8" />
