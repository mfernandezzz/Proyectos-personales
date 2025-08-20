#1)Crear un programa que permita gestionar una lista de tareas pendientes y completadas, incluyendo la funcionalidad de tareas
#compuestas con subtareas. 
#- Crear una clase Tarea que represente una tarea individual con los atributos: nombre y completada (valor booleano). Implementar
#el constructor de la clase Tarea que tome como argumento el nombre de la tarea. El atributo completada debera tener False por defecto.
#Definir un metodo que cambie el status de la Tarea a completada.

#2)Crear una Subclase llamada TareaCompuesta que herede de la clase Tarea. Esta SubClase permitira gestionar tareas que contienen subtareas.
#La clase TareaCompuesta tendra el atributo adicional subtareas, el cual sera una lista vacia que almacenara objetos de tipo Tarea.
#Se debe redefinir el constructor de la clase Tarea y agregarle el atributo extra.
#Definir un metodo en la subclase que permita agregar una subtarea (objeto Tarea) a la lista de subtareas.
#Sobreescribir el metodo marcar_completada() para marcar la tarea compuesta como completada, asi como tambien marcar como completadas
#todas sus subtareas.

#3)Crea una clase llamada gestor_tareas() que administra las listas de tareas pendientes y completadas, incluyendo tareas compuestas.
#La clase tendra los siguientes atributos, ambos inicializados como listas vacias:
#tareas_pendientes: una lista que almacenara objetos de tipo tarea representando las tareas pendientes. 
#tareas_completadas: una lista que almacenara objetos de tipo tarea representando las tareas completadas. 

#4)Define los siguientes metodos en la clase Gestor_tareas:
#- agregar_tarea_pendiente(tarea): este metodo toma como argumento un objeto de tipo Tarea (o tareaCompuesta), y lo agrega a la lista de
#tareas pendientes.
#- completar_tarea(tarea): este metodo toma como argumento un objeto de tipo tarea (o TareaCompuesta), busca esa tarea en la lista 
#tareas_pendientes, la marca como completada utilizando el metodo marcar_completada() y la mueve a la lista tareas_completadas.
#- mostrar_tareas(): este metodo imprime en pantalla la lista de tareas pendientes y la lista de tareas completadas, indicando su
#estado (completada o no completada).

class Tarea:
    def __init__(self, nombre): 
        self.nombre = nombre
        self.completada = False #las tareas estaran incompletas por defecto

    def marcar_completada(self):
        self.completada = True #metodo que marca una tarea como completada

class TareaCompuesta(Tarea): #TareaCompuesta hereda de la clase Tarea
    def __init__(self, nombre):
        super().__init__(nombre) #se redefine el metodo de la superclase Tarea
        self.subtareas = [] #se le agrega a la subclase TareaCompuesta el atributo subtareas, que sera una lista vacia

    def agregar_subtarea(self, tarea): #objeto de tipo tarea
        self.subtareas.append(tarea) #se agrega un objeto de tipo Tarea a la lista subtareas
        print(f'La tarea {tarea.nombre} ha sido agregada a la lista subtareas.')

    def marcar_completada(self):
        super().marcar_completada() #se redefine el metodo de la superclase Tarea
        for s in self.subtareas: #se itera en todos los objetos dentro de la lista subtareas
            s.marcar_completada() #todas las subtareas se marcan como completadas

class GestorTareas:
    def __init__(self): #esta clase contendra dos atributos con listas vacias, para tareas pendientes y completadas
        self.tareas_pendientes = []
        self.tareas_completadas = []

    def agregar_tarea_pendiente(self, tarea): 
        self.tareas_pendientes.append(tarea) #recibe un objeto Tarea o TareaCompuesta y lo agrega a la lista pendientes

    def completar_tarea(self, tarea): #recibe un objeto Tarea o TareaCompuesta
        if tarea in self.tareas_pendientes: #si el objeto se encuentra en la lista pendientes
            tarea.marcar_completada() #se marca la tarea como completada
            self.tareas_completadas.append(tarea) #el objeto es agregado a la lista completadas
            self.tareas_pendientes.remove(tarea) #el objeto es removido de la lista pendientes
            print('La tarea ha sido completada y eliminada de la lista pendientes.')
        else:
            print('La tarea no ha sido encontrada dentro de la lista pendientes.')

    def listar_tareas(self): #se lista el nombre de los objetos dentro de la lista pendientes y completadas
        print('Tareas Pendientes')
        for p in self.tareas_pendientes:
            print(p.nombre)
        
        print('Tareas completadas')
        for c in self.tareas_completadas:
            print(c.nombre)

primer_tarea = Tarea('preparar la comida')
segunda_tarea = Tarea('ir de compras')
tercera_tarea = Tarea('llamar al servicio tecnico')
print(primer_tarea.completada)
segunda_tarea.marcar_completada()
print(segunda_tarea.completada)

primer_t_compuesta = TareaCompuesta('limpiar el jardin')
subtarea_uno = Tarea('cortar cesped')
subtarea_dos = Tarea('podar arboles')
subtarea_tres = Tarea('regar las plantas')
print(primer_t_compuesta.nombre)
print(primer_t_compuesta.subtareas)
primer_t_compuesta.agregar_subtarea(subtarea_uno)
primer_t_compuesta.agregar_subtarea(subtarea_dos)
primer_t_compuesta.agregar_subtarea(subtarea_tres)
print(primer_t_compuesta.subtareas)

print(primer_t_compuesta.completada)
print(subtarea_uno.completada)
print(subtarea_dos.completada)
print(subtarea_tres.completada)
primer_t_compuesta.marcar_completada()
print(primer_t_compuesta.completada)
print(subtarea_uno.completada)
print(subtarea_dos.completada)
print(subtarea_tres.completada)

segunda_t_compuesta = TareaCompuesta('lavar la ropa')
subtarea_cuatro = Tarea('colgar la ropa')
subtarea_cinco = Tarea('entrar la ropa')
subtarea_seis = Tarea('guardar la ropa')
subtarea_siete = Tarea('ordenar el ropero')

gestionador = GestorTareas()
gestionador.agregar_tarea_pendiente(segunda_t_compuesta)
gestionador.agregar_tarea_pendiente(subtarea_cuatro)
gestionador.agregar_tarea_pendiente(subtarea_cinco)
gestionador.agregar_tarea_pendiente(subtarea_seis)
gestionador.listar_tareas()
gestionador.completar_tarea(segunda_t_compuesta)
print(segunda_t_compuesta.completada)
gestionador.listar_tareas()
gestionador.completar_tarea(subtarea_siete)
print(subtarea_siete.completada)
