# 👁️‍🗨️ Detección de Personas con Inteligencia Artificial — Mini Hackathon

## 🧠 Objetivo del Proyecto

Desarrollar un programa en **Python** que:
- Tome una foto usando la cámara web.
- Envíe la imagen a una **API de Inteligencia Artificial** para detectar si hay una persona en ella.
- Devuelva un resultado indicando si se detectó o no una persona.
- (Opcional) Reconozca también otros objetos en la imagen.

Este proyecto fue realizado como parte de un reto de hackatón con fines educativos, donde se busca fomentar el aprendizaje y el uso de herramientas de IA apoyados por asistentes inteligentes como Claude, Copilot y ChatGPT.

---

## 🧪 Documentación del Proceso de Investigación

Durante el desarrollo investigamos varias APIs que ofrecen servicios de detección de objetos y personas. Consultamos modelos tanto de pago como gratuitos y evaluamos su facilidad de integración con Python.

### 🔍 Fuentes utilizadas:
- **GitHub Copilot**
- **Claude 3.7 Sonnet**
- **ChatGPT (como consultor técnico senior)**

### 📋 Prompts utilizados:

**Prompt en GitHub Copilot:**
> Estoy trabajando en un programa que tome una foto, y luego detecte si en esa foto hay una persona o no. Pero para esto necesito trabajar con una API que me haga este trabajo, y que sea compatible con Python.  
> Quiero que me des una lista de 10 APIs y servicios, ordenadas de manera que la primera sea la mejor.

**Prompt en Claude:**
> Estoy trabajando en un proyecto para un hackathon donde necesito implementar detección de personas usando inteligencia artificial. Me han sugerido varias APIs y servicios: Clarifai, Roboflow, Google Cloud Vision API, Azure Computer Vision, Hugging Face con YOLO.  
> ¿Podrías ordenarlas de la menos recomendable a la más recomendable para un proyecto de hackathon con tiempo limitado?  
> Además, ¿podrías darme un breve ejemplo de código para implementar la opción más recomendada en Python?

### ✅ APIs Evaluadas:

| API                      | Facilidad de uso | Gratuita | Requiere registro | Justificación                                  |
|--------------------------|------------------|----------|-------------------|------------------------------------------------|
| Hugging Face Inference API | ⭐⭐⭐⭐⭐           | Sí       | Sí                | ✅ Ofrece modelos como `detr-resnet-50`, fácil integración con Python |
| Roboflow                | ⭐⭐⭐⭐             | Sí       | Sí                | Potente, pero requiere configuración previa de proyecto |
| Clarifai                | ⭐⭐⭐              | Limitada | Sí                | Buen soporte pero más complejo de implementar |
| Google Cloud Vision     | ⭐⭐⭐              | No       | Sí                | Requiere configuración extensa y tarjeta de crédito |
| Azure Computer Vision   | ⭐⭐               | No       | Sí                | Similar a Google, complejo para un hackathon rápido |

### 🥇 API Elegida: **Hugging Face Inference API**
- Tiene una **interfaz sencilla con solicitudes HTTP**.
- Soporta modelos de **detección de objetos como DETR (facebook/detr-resnet-50)**.
- Compatible con Python mediante `requests`.
- Requiere un token gratuito (se obtiene al crear una cuenta).

---

## 🧰 Tecnologías y Librerías Usadas

- Python 3.x
- `opencv-python` — Para capturar imágenes desde la cámara web.
- `requests` — Para interactuar con la API de Hugging Face.
- `pillow` — Para manejo opcional de imágenes.
- API de Hugging Face — Modelo: `facebook/detr-resnet-50`

Instalación rápida:
```bash
pip install opencv-python requests pillow
