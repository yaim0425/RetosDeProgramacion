# 🔤 Reto: Contar palabras en un texto

## Enunciado

Crea un programa que **cuente cuántas veces se repite cada palabra** en un texto dado y **muestre el recuento final**.

### Reglas:

- Los **signos de puntuación no forman parte** de las palabras.
- Una **palabra es igual aunque esté en mayúsculas o minúsculas**.
- No se pueden utilizar funciones propias del lenguaje que resuelvan el problema automáticamente (como `collections.Counter`, expresiones regulares, etc.).

## 💡 Ejemplo de uso

```python
count_words("¡Hola mundo! hola, Mundo.")  
# {
#   "hola": 2,
#   "mundo": 2
# }
```

## 🐍 Lenguaje
Las soluciones están escritas en **Python**.

## ✅ Objetivo
Este reto pone en práctica:
- Procesamiento de texto sin funciones avanzadas
- Normalización de datos (mayúsculas/minúsculas)
- Uso de diccionarios para conteo manual
- Estructuras de control y lógica condicional

## 📁 Archivo relacionado
- [`word_count.py`](./word_count.py)
