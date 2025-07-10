def word_count(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

# Ejemplo de uso
print(word_count("¡Hola! ¿Cómo estás? Hola, hola... estoy bien, ¿y tú?"))                    # {'hola': 3, 'cómo': 1, 'estás': 1, 'estoy': 1, 'bien': 1, 'y': 1, 'tú': 1}
print(word_count("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")) # {'hola': 1, 'mi': 2, 'nombre': 2, 'es': 2, 'brais': 1, 'completo': 1, 'mouredev': 1}
print(word_count("Python es un lenguaje de programación. Python es fácil de aprender."))     # {'python': 2, 'es': 2, 'un': 1, 'lenguaje': 1, 'de': 2, 'programación': 1, 'fácil': 1, 'aprender': 1}