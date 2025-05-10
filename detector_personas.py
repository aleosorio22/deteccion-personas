import cv2
import requests
import os
from PIL import Image
import io
import base64
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def capturar_imagen():
    """Captura una imagen desde la cámara web y la guarda como 'captura.jpg'"""
    # Inicializar la cámara web (0 es generalmente la cámara predeterminada)
    camara = cv2.VideoCapture(0)
    
    # Verificar si la cámara se abrió correctamente
    if not camara.isOpened():
        print("Error: No se pudo acceder a la cámara web.")
        return False
    
    # Capturar un fotograma
    ret, fotograma = camara.read()
    
    # Liberar la cámara
    camara.release()
    
    if not ret:
        print("Error: No se pudo capturar la imagen.")
        return False
    
    # Guardar la imagen
    cv2.imwrite('captura.jpg', fotograma)
    print("Imagen guardada como 'captura.jpg'")
    return True

def detectar_persona(ruta_imagen):
    """Envía la imagen a la API de Hugging Face para detectar personas"""
    API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
    
    # Obtener el token de API desde las variables de entorno
    API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
    
    if not API_TOKEN:
        print("Error: No se encontró la API_TOKEN en el archivo .env")
        return None

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "image/jpeg"
    }

    # Cargar la imagen en formato binario
    with open(ruta_imagen, "rb") as f:
        imagen = f.read()

    response = requests.post(API_URL, headers=headers, data=imagen)

    if response.status_code == 200:
        resultado = response.json()
        # Buscar si hay una persona entre los objetos detectados
        for deteccion in resultado:
            if "label" in deteccion and deteccion["label"] == "person":
                return True
        return False
    else:
        print(f"Error en la API: {response.status_code}")
        print(response.text)
        return None

def main():
    # Capturar la imagen
    if capturar_imagen():
        # Detectar si hay una persona en la imagen
        resultado = detectar_persona("captura.jpg")
        
        if resultado is True:
            print("Persona detectada")
        elif resultado is False:
            print("No se detectó persona")
        else:
            print("No se pudo realizar la detección")

if __name__ == "__main__":
    main()