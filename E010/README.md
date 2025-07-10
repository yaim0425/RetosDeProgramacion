# 🔄 Reto: Conversor de texto ↔ código morse

## Enunciado

Crea un programa que sea capaz de **transformar texto natural a código morse y viceversa**.

### Reglas:

- El programa debe **detectar automáticamente** si la entrada está en texto o en morse, y realizar la conversión correspondiente.
- En morse se usan:
  - Punto `.` para indicar un "dit"
  - Raya `—` para un "dah"
  - Un **espacio** entre letras o símbolos
  - **Dos espacios** entre palabras
- No se deben usar librerías que realicen la conversión automáticamente.
- El alfabeto morse soportado será el mostrado en:
  [Wikipedia - Código Morse](https://es.wikipedia.org/wiki/Código_morse)

## 💡 Ejemplo de uso

```python
convert("Hola Mundo")  
# .... --- .-.. .-  -- ..- -. -.. ---  

convert(".... --- .-.. .-  -- ..- -. -.. ---")  
# hola mundo
```

## 🐍 Lenguaje
Las soluciones están escritas en **Python**.

## ✅ Objetivo
Este reto pone en práctica:
- Manipulación de cadenas y estructuras de datos
- Conversión entre representaciones textuales
- Diseño de lógica para detección automática de formato
- Trabajo con diccionarios bidireccionales (texto <-> morse)

## 📁 Archivo relacionado
- [`morse_converter.py`](./morse_converter.py)
