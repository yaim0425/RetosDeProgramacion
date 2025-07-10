# Morse code dictionary
text_to_morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "ñ": "--.--",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",

    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}

# Reverse dictionary
morse_to_text = {v: k for k, v in text_to_morse.items()}


def is_morse(text):
    for char in text:
        if char not in ".- ":
            return False
    return True


def to_morse(text):
    text = text.lower()
    result = []
    for word in text.split(" "):
        codes = []
        for char in word:
            if char in text_to_morse:
                codes.append(text_to_morse[char])
        result.append(" ".join(codes))
    return "  ".join(result)


def to_text(morse):
    result = []
    words = morse.strip().split("  ")
    for word in words:
        letters = word.split()
        result.append("".join(morse_to_text.get(code, "?") for code in letters))
    return " ".join(result)


def convert(text):
    if is_morse(text):
        return to_text(text)
    else:
        return to_morse(text)


# Ejemplo de uso
example_1 = "Feliz año nuevo"
example_2 = "..-. . .-.. .. --..  .- --.-- ---  -. ..- . ...- ---"

print("Text to Morse:")
print(convert(example_1))  # ..-. . .-.. .. --..  .- --.-- ---  -. ..- . ...- ---

print("\nMorse to Text:")
print(convert(example_2))  # Feliz año nuevo
