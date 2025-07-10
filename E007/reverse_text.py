def reverse_text(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text

# Ejemplo de uso
print(reverse_text("Hola mundo")) # "odnum aloH"
print(reverse_text("Python"))     # "nohtyP"
