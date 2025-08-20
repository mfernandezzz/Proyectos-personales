#Proyecto de gestion de biblioteca
#Crea un sistema para gestionar una biblioteca. Puedes incluir clases como libro, usuario y biblioteca. Sus funcionalidades pueden ser:
#Libro: atributos como titulo, autor, editorial y metodos para mostrar informacion.
#Usuario: atributos como nombre, id de usuario, devolver un libro
#Biblioteca: metodos para añadir libros, prestar libros, registrar y eliminar usuarios.
class Libro:
    def __init__(self, titulo, autor, editorial):
        self.titulo = str.upper(titulo)
        self.autor = autor
        self.editorial = editorial

class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.libros_en_posesion = []
        self.registrado = False

    def libros_poseidos(self): #libros en posesion por parte de un usuario
        for lib in self.libros_en_posesion:
            print(f'Titulo del libro: {lib.titulo}')

    def devolver_libro(self, libro): #objeto libro. Metodo para que el usuario devuelva un libro
        biblioteca_nacional.libros.append(libro) #el objeto libro se agrega a la lista libros de la biblioteca
        self.libros_en_posesion.remove(libro) #el usuario deja de poseer el libro, se elimina de la lista libros en posesion
        biblioteca_nacional.libros_en_prestamo.remove(libro.titulo) #se elimina el titulo del libro en la lista libros en prestamo (biblioteca)
        print('Libro devuelto')

class Biblioteca:
    def __init__(self):
        self.usuarios = [] #usuarios registrados
        self.libros = [] #libros disponibles
        self.libros_en_prestamo = [] #titulos de los libros en prestamo

    def usuarios_registrados(self): #mostrar todos los usuarios registrados
        print('Usuarios:')
        for user in self.usuarios:
            print(f'Nombre: {user.nombre} - ID: {user.id}')

    def listar_libros(self): #mostrar los libros disponibles
        print('Libros:')
        for lib in self.libros:
            print(f'{lib.titulo} - {lib.autor} - {lib.editorial}')

    def libros_prestados(self): #mostrar el titulo de un libro prestado
        print('Libros en prestamo:')
        for l in self.libros_en_prestamo:
            print(l)

    def buscar_libro(self, titulo): #titulo del libro
        disp = [l.titulo for l in self.libros if l.titulo == titulo] #lista que almacena el titulo de un libro
        if titulo in disp: #si el titulo a buscar se encuentra en la lista
            print(f'Libro disponible. Cantidad de existencias: {len(disp)}') #se muestra la cantidad de existencias
        else:
            print('Libro no disponible')

    def añadir_libro(self, libro): #añadir un libro
        self.libros.append(libro)
        print(f'Libro {libro.titulo} añadido a la biblioteca.')

    def registrar_usuario(self, usuario): #objeto usuario, registrar un usuario
        usuario.registrado = True #el atributo usuario registrado cambia a True
        self.usuarios.append(usuario) #se agrega al usuario a la lista usuarios
        print(f'Usuario {usuario.nombre} registrado.')

    def baja_usuario(self, usuario): #objeto usuario
        usuario.registrado = False #el atributo usuario registrado cambia a False
        self.usuarios.remove(usuario) #se remueve de la lista al usuario
        print(f'El usuario {usuario.nombre} ha sido quitado del registro.')

    def prestar_libro(self, libro, usuario): #objeto libro y usuario
        if (libro in self.libros) and (usuario in self.usuarios): #si el libro esta disponible y el usuario esta registrado
            self.libros_en_prestamo.append(libro.titulo) #se agrega el titulo del libro a la lista libro_en_prestamo
            self.libros.remove(libro) #se remueve el libro de la lista libros
            usuario.libros_en_posesion.append(libro) #se agrega el libro a la lista del usuario
            print(f'El libro {libro.titulo} ha sido prestado al usuario {usuario.nombre}.')
        else:
            print('No se puede prestar el libro')

    def editar_informacion_libro(self, libro): #editar informacion de un libro
        libro.titulo = str.upper(input('Nombre del libro: '))
        libro.autor = str(input('Nombre de autor: '))
        libro.editorial = str(input('Nombre de la editorrial: '))

biblioteca_nacional = Biblioteca()

usuarioUno = Usuario('Jonathan', 567)
usuarioDos = Usuario('Ernesto', 467)
usuarioTres = Usuario('Geovanna', 483)

libro_uno = Libro('Arte de la guerra', 'Sun Tzu', 'Abracadabra')
libro_dos = Libro('1984', 'George Orwell', 'Tiempos pasados')
libro_tres = Libro('Farenheit', 'Ray Bradbury', 'Distopic')
libro_cuatro = Libro('El poder del ahora', 'Eckart Tolle', 'desc')
libro_cinco = Libro('Diccionario Enciclopedico', 'Santillana', 'Santillana')
libro_seis = Libro('La guerra de los hechiceros', 'Sara Burnley', 'Magic World')
libro_siete = Libro('Caperucita Roja', 'Los hermanos Grim', 'Warner Bros')
libro_ocho = Libro('Caperucita Roja', 'Los hermanos Grim', 'Warner Bros')
libro_nueve = Libro('Caperucita Roja', 'Los hermanos Grim', 'Warner Bros')
libro_diez = Libro('Caperucita Roja', 'Los hermanos Grim', 'Warner Bros')

biblioteca_nacional.añadir_libro(libro_uno)
biblioteca_nacional.añadir_libro(libro_dos)
biblioteca_nacional.añadir_libro(libro_tres)
biblioteca_nacional.añadir_libro(libro_cuatro)
biblioteca_nacional.añadir_libro(libro_cinco)
biblioteca_nacional.añadir_libro(libro_siete)
biblioteca_nacional.añadir_libro(libro_ocho)
biblioteca_nacional.añadir_libro(libro_nueve)
biblioteca_nacional.añadir_libro(libro_diez)
biblioteca_nacional.listar_libros()
biblioteca_nacional.registrar_usuario(usuarioUno)
biblioteca_nacional.registrar_usuario(usuarioDos)
biblioteca_nacional.usuarios_registrados()
#biblioteca_nacional.prestar_libro(libro_seis, usuarioDos)
biblioteca_nacional.prestar_libro(libro_uno, usuarioUno)
biblioteca_nacional.prestar_libro(libro_dos, usuarioUno)
biblioteca_nacional.prestar_libro(libro_tres, usuarioUno)
biblioteca_nacional.prestar_libro(libro_cuatro, usuarioDos)
biblioteca_nacional.prestar_libro(libro_cinco, usuarioDos)
biblioteca_nacional.libros_prestados()
#usuarioUno.libros_poseidos()
#biblioteca_nacional.baja_usuario(usuarioDos)
#biblioteca_nacional.usuarios_registrados()
biblioteca_nacional.añadir_libro(libro_seis)
#biblioteca_nacional.editar_informacion_libro(libro_seis)
biblioteca_nacional.listar_libros()
usuarioUno.libros_poseidos()
#usuarioUno.devolver_libro(libro_uno)
#usuarioUno.devolver_libro(libro_dos)
#usuarioUno.devolver_libro(libro_tres)
#biblioteca_nacional.libros_prestados()
#biblioteca_nacional.listar_libros()
#biblioteca_nacional.buscar_libro(str.upper('la guerra de los hechiceros'))
