import random
items = [ #posibles caracteres que tendra la contraseña
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', 
    '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', 
    '%', '&', '*', '0', '@', '#', '$', '%', '&', '*', 
    '(', ')', '-', '_', '+', '-', '/', '=', '[', ']', 
    '{', '}', '|', ';', ':', '<', '>', ',', '.', '?', 
    '¿', '¡', '!', 'º', 'ª', 'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
]
lenght = int(input('Cantidad de caracteres que tendra la contraseña: '))
def generate(lenght):
    password = ''
    for i in range(lenght): 
        i = random.choice(items) #se obtiene los caracteres de la contraseña
        password += i #se agregan los caracteres al string final
    return password
print(generate(lenght))
