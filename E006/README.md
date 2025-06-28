# 🧠 Reto: Calcular Aspect Ratio

## Enunciado

Crea un programa que se encargue de **calcular el _aspect ratio_ de una imagen a partir de una URL**.

### Reglas:

- El programa debe descargar la imagen desde una **URL proporcionada**.
- A partir de sus dimensiones (ancho y alto), debe **calcular y retornar el aspect ratio** en formato clásico `ancho:alto`.
- El resultado debe estar simplificado, por ejemplo:
  - 1920x1080 → `16:9`
  - 1280x720 → `16:9`
  - 1024x768 → `4:3`

## 💡 Ejemplo de uso

```python
get_aspect_ratio("https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png")
# 1:1
```

## 🐍 Lenguaje
La solución está escrita en **Python**.

## ✅ Objetivo
Este reto pone en práctica:
- Descarga y manejo de archivos desde la red
- Lectura de imágenes y sus metadatos
- Cálculo matemático para reducción de fracciones

## 📁 Archivo relacionado
- [`aspect_ratio.py`](./aspect_ratio.py)
