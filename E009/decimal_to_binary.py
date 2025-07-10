def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary

# Ejemplo de uso
print(decimal_to_binary(0))    # "0"
print(decimal_to_binary(5))    # "101"
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1024)) # "10000000000"
