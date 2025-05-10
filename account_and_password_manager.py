import string, random
caracteres = [] #lista que almacenara los posibles caracteres que tendra la contraseña final
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = [',', ';', '.', ':', '-', '_', '!', '¡', '@', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '*', '+', '[', ']', '{', '}', '<', '>', '|', 'º', 'ª']
#se agregan elementos a la lista caracteres
caracteres.extend(simbolos) 
caracteres.extend(list(string.ascii_lowercase)) #letras en minuscula
caracteres.extend(list(string.ascii_uppercase)) #letras en mayuscula
caracteres.extend(numeros)
#Funcion que genera una contraseña
def password(caracteres):
    passwordL, passwordF = [], ''
    char = int(input('Ingrese la cantidad de caracteres que tendra tu contraseña, minimo ocho: '))
    while char < 8: #el bucle se repetira hasta que el usuario ingrese un numero igual o mayor a ocho
        print('Tu contraseña debe tener como minimo 8 caracteres.')
        char = int(input('Ingrese la cantidad de caracteres que tendra tu contraseña, minimo ocho: '))
    while len(passwordL) < char:
        add = random.choice(caracteres) #se toman elementos al azar de la lista caracteres
        passwordL.append(add) #se almacenan dichos elementos en passwordL
    passwordF = ''.join(passwordL) #se toman los elementos de la lista passwordL para generar el string final
    return passwordF #se devuelve la contraseña

#Gestor de Cuentas y Contraseñas
#Funcion para agregar una cuenta con su respectiva contraseña
def agregar(gestor, cuenta, contraseña):
    gestor[cuenta] = contraseña
    print(f'La cuenta de {cuenta} a sido agregada con la contraseña {contraseña}')

#Funcion para eliminar una cuenta
def eliminar(gestor, cuenta):
    if cuenta in gestor.keys(): #si la cuenta se encuentra como clave en el diccionario
        gestor.pop(cuenta) #la cuenta se elimina
        print(f'La cuenta de {cuenta} ha sido eliminada.')
    else:
        print(f'La cuenta de {cuenta} no fue encontrada.')

#Funcion para buscar y mostrar una cuenta con su respectiva contraseña
def buscar(gestor, cuenta):
    if cuenta in gestor.keys(): #si la cuenta se encuentra como clave en el diccionario
        print(f'Cuenta: {cuenta} Contraseña: {gestor[cuenta]}') #se muestra la cuenta y su contraseña
    else:
        print(f'La cuenta de {cuenta} no fue encontrada.')

#Funcion para mostrar todas las cuentas con sus contraseñas
def mostrar(gestor):
    if gestor: #si el diccionario tiene elementos
        for cuenta, contraseña in gestor.items(): #se itera en las claves y los valores del diccionario
            print(f'Cuenta: {cuenta} Contraseña: {contraseña}') #se devuelve las cuentas y sus contraseñas
    else:
        print('El gestor de cuentas y contraseñas esta vacio.') #mensaje de error si el diccionario esta vacio

#Funcion para modificar la contraseña a una cuenta
def modificarContraseña(gestor, cuenta, nuevaContraseña):
    if cuenta in gestor.keys(): #si la cuenta a la que le vamos a cambiar la contraseña se encuentra como clave en el dict
        gestor[cuenta] = nuevaContraseña #se le asigna la nueva contraseña
        print(f'Contraseña modificada a la cuenta de {cuenta}')
    else:
        print(f'No se ha encontrado la cuenta {cuenta}')

def gestorCuentasContraseñas():
    gestor = {} #diccionario que almacenara las cuentas como clave y contraseñas como valores
    while True: #el bucle se repetira una y otra vez para que el usuario interactue con las opciones
        print('Opciones')
        print('1. Agregar cuenta')
        print('2. Eliminar cuenta')
        print('3. Buscar cuenta')
        print('4. Mostrar cuentas y sus contraseñas')
        print('5. Modificar contraseña')
        print('6. Salir del gestor')
        opcion = int(input('Opcion: ')) #el usuario introduce una opcion
        if opcion == 1:
            cuenta = str.upper(input('Ingrese el nombre de la cuenta: '))
            contraseña = password(caracteres) #se genera una nueva contraseña para la nueva cuenta
            agregar(gestor, cuenta, contraseña)
        elif opcion == 2:
            cuenta = str.upper(input('Ingrese la cuenta que desea eliminar: '))
            eliminar(gestor, cuenta)
        elif opcion == 3:
            cuenta = str.upper(input('Ingrese la cuenta que desea buscar: '))
            buscar(gestor, cuenta)
        elif opcion == 4:
            mostrar(gestor)
        elif opcion == 5:
            cuenta = str.upper(input('Ingrese la cuenta para modificar su contraseña: '))
            nuevaContraseña = password(caracteres) #se genera una nueva contraseña para la cuenta modificada
            modificarContraseña(gestor, cuenta, nuevaContraseña)
        elif opcion == 6:
            print('Saliendo del Gestor de Cuentas y Contraseñas')
            break #el bucle finaliza
        else:
            print('Opcion incorrecta')
    return ''

print(gestorCuentasContraseñas())
