# 🧮 Reto: Área de polígonos

## Enunciado

Crea una única **función** que sea capaz de **calcular y retornar el área de un polígono**.

### Reglas:

- La función debe recibir **solo un polígono a la vez** como parámetro.
- Los **tipos de polígono soportados** son:
  - Triángulo
  - Cuadrado
  - Rectángulo
- La función debe **imprimir el área** de **un polígono de cada tipo**.

## 💡 Ejemplo de uso

```python
calculate_area({"type": "triangle", "base": 10, "height": 5})     # 25.0
calculate_area({"type": "square", "side": 4})                     # 16
calculate_area({"type": "rectangle", "width": 6, "height": 3})    # 18
```

## 🐍 Lenguaje
Las soluciones están escritas en **Python**.

## ✅ Objetivo
Este reto pone en práctica:
- Diseño de funciones flexibles
- Uso de estructuras de datos como diccionarios
- Condicionales y lógica estructurada

## 📁 Archivo relacionado
- [`polygon_area.py`](./polygon_area.py)