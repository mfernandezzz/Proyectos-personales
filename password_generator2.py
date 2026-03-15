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
length = input('Cantidad de caracteres que tendra la contraseña: ')
while not(length.isdigit()) or (int(length) < 8):
        print('Valor incorrecto. Ingrese nuvamente.')
        length = input('ingrese la cantidad de caracteres que tendra la contraseña (min 8): ')

def generate(length):
    password = '' #variable que almacenara el string con la contraseña final
    for i in range(int(length)): 
        i = random.choice(items) #se obtiene los caracteres de la contraseña
        password += i #se agregan los caracteres al string final
    return password

print(generate(length))
