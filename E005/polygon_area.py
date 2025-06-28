def calculate_area(form, base, height=None):
    if form == "triangle":
        return (base * height) / 2

    elif form == "square":
        return base**2

    elif form == "rectangle":
        return base * height

    raise ValueError("Forma invalida.")

# Ejemplo de uso
print(calculate_area("triangle", 10, 5))  # 25.0
print(calculate_area("square", 4))        # 16
print(calculate_area("rectangle", 6, 3))  # 18
