def is_anagram(word1, word2):
    # Normalizamos a minúsculas
    word1 = word1.lower()
    word2 = word2.lower()

    # Si son iguales, no son anagramas
    if word1 == word2:
        return False

    # Ordenamos y comparamos las letras
    return sorted(word1) == sorted(word2)

# Probar la función con diferentes casos
print(is_anagram("amor", "roma"))
print(is_anagram("amor", "amor"))
print(is_anagram("listen", "silent"))
print(is_anagram("perro", "gato"))
