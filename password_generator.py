import string, random
caracteres = [] #se crea la lista que contendra los caracteres que conformaran la contraseña final
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = [',', ';', '.', ':', '-', '_', '!', '¡', '@', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '*', '+', '[', ']', '{', '}', '<', '>', '|', 'º', 'ª']
#se agrega a la lista caracteres, signos ortograficos, numeros, letras en mayuscula y en minuscula.
caracteres.extend(simbolos)
caracteres.extend(list(string.ascii_uppercase))
caracteres.extend(numeros)
caracteres.extend(list(string.ascii_lowercase))

def password():
    passwordL, password = [], '' #se define una lista y un string, ambos vacios

    num_char = input('ingrese la cantidad de caracteres que tendra la contraseña (min 8): ')
    while not(num_char.isdigit()) or (int(num_char) < 8): #se comprueba que lo introducido por el usuario sea un valor valido
        print('Valor incorrecto. Ingrese nuvamente.') #mensaje de error
        num_char = input('ingrese la cantidad de caracteres que tendra la contraseña (min 8): ')

    while len(passwordL) < (int(num_char)): #condicion para introducir elementos en la lista vacia
        c = random.choice(caracteres) #se escoge un elemento al azar de la lista caracteres
        passwordL.append(c) #se agrega el elemento a la lista
        password = ''.join(passwordL) #string con la contraseña final

    return f'La contraseña generada es: {password}.'

print(password())
