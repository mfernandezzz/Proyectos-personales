#Crear un programa que simule una agenda de contactos, usando clases.
class AgendaContactos: #clase que permite crear una Agenda para administrar objetos contacto
    def __init__(self):
        self.contactos = []

    def listar_contactos(self): #lista el valor de los atributos de cada contacto
        for c in self.contactos:
            print(f'Nombre: {c.nombre} Numero: {c.numero} Email: {c.email}')

    def agregar_contacto(self, contacto): #objeto contacto
        self.contactos.append(contacto)
        print(f'Contacto {contacto.nombre} Agregado')

    def eliminar_contacto(self, contacto): #objeto contacto
        if contacto in self.contactos:
            print(f'Contacto {contacto.nombre} removido')
            self.contactos.remove(contacto)
        else:
            print(f'Contacto {contacto.nombre} no encontrado')

    def buscar_contacto(self, contacto): #recibe un objeto contacto, lo busca en la lista y devuelve el valor de sus atributos numero e email
        if contacto in self.contactos:
            print(f'Numero: {contacto.numero}')
            print(f'Email: {contacto.email}')
        else:
            print(f'El contacto {contacto.nombre} no fue encontrado.')

    def editar_contacto(self, contacto): #recibe un objeto contacto y le asigna nuevos valores a sus atributos
        if contacto in self.contactos:
            contacto.nombre = str.upper(input('Ingrese el nuevo nombre del contacto: '))
            contacto.numero = int(input('Ingrese el nuevo numero del contacto: '))
            contacto.email = str.lower(input('Ingrese el nuevo Email del contacto: '))
            print('Contacto modificado')
        else:
            print(f'Contacto {contacto.nombre} no encontrado')

class Contacto: #clase que permite crear objetos contacto
    def __init__(self, nombre, numero, email):
        self.nombre = str.upper(nombre)
        self.numero = int(numero)
        self.email = str.lower(email) 

agenda = AgendaContactos()
contactoUno = Contacto('Adrian', 97628741, 'adrian@gmail.com')
contactoDos = Contacto('Sebastian', 98367422, 'sebastian@gmail.com') 
contactoTres = Contacto('Esteban', 99258463, 'esteban@gmail.com')
contactoCuatro = Contacto('Pedro', 91561483, 'pedro@gmail.com')

agenda.agregar_contacto(contactoUno)
agenda.agregar_contacto(contactoDos)
agenda.agregar_contacto(contactoTres)

agenda.listar_contactos()

agenda.buscar_contacto(contactoDos) #se busca el contacto y se muestra su numero e email
agenda.buscar_contacto(contactoCuatro) #el contacto no es encontrado

agenda.eliminar_contacto(contactoUno) #se elimina el contacto
agenda.eliminar_contacto(contactoCuatro) #el contacto no es encontrado

agenda.editar_contacto(contactoTres) #se busca y edita el contacto
agenda.editar_contacto(contactoCuatro) #el contacto no es encontrado

agenda.listar_contactos() #se listan los contactos existentes
