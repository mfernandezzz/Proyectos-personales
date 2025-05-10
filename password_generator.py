import string, random
caracteres = []#se crea la lista que contendra los caracteres que conformaran la contraseña final
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = [',', ';', '.', ':', '-', '_', '!', '¡', '@', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '*', '+', '[', ']', '{', '}', '<', '>', '|', 'º', 'ª']
#se agrega a la lista caracteres signos ortograficos, numeros, letras en mayuscula y en minuscula.
caracteres.extend(simbolos)
caracteres.extend(list(string.ascii_uppercase))
caracteres.extend(numeros)
caracteres.extend(list(string.ascii_lowercase))

def password(caracteres):
    char = int(input('¿Cuantos caracteres tendra tu contraseña? ingrese un numero mayor o igual a 8: '))
    passwordL, password = [], ''
    while char < 8:#la contraseña debe tener como minimo 8 caracteres
        print('Debe ingresar un numero mayor o igual a 8')
        char = int(input('¿Cuantos caracteres tendra tu contraseña? ingrese un numero mayor o igual a 8: '))
    while len(passwordL) < char:
        add = random.choice(caracteres)#se obtiene elementos de la lista caracteres
        passwordL.append(add)#se agrega elementos a la lista
        password = ''.join(passwordL)#se agregan los caracteres al string con la contraseña final
    return password
print(f'La contraseña generada es: {password(caracteres)}')
