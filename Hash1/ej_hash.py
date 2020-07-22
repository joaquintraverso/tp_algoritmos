from tda_hash import *
from tda_lista import nodoLista, Lista, insertar, eliminar, busqueda, barrido, tamanio, lista_vacia, criterio, barrido_con_sublista
from random import randint, choice

#Ej 1

'''
class Palabra(object):
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

    def __str__(self):
        return self.palabra + ': ' + self.significado

tabla = crear_tabla(28)

dato = Palabra('Agua', 'Sustancia líquida')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')
dato = Palabra('Gato', 'Mamifero felino')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')
dato = Palabra('Perro', 'Mamifero carnivero domestico')
agregar_ta(tabla, hash_diccionario, dato, 'palabra')

barrido_ta(tabla)

pos = buscar_ta(tabla, hash_diccionario, Palabra('Agua',''), 'palabra')
if pos is not None:
    print('\nLa palabra existe \n', pos.info)

pos = buscar_ta(tabla, hash_diccionario, Palabra('Gato',''), 'palabra')
if pos is not None:
    print('\nSe elimino la palabra', pos.info.palabra)
    quitar_ta(tabla, hash_diccionario, Palabra('Gato',''), 'palabra')
'''

#Ej 02

'''
class Guia(object):
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return self.apellido + " " + self.nombre + ": " + str(self.numero) + "\n- " + self.direccion

tabla = crear_tabla(10)

dato = Guia(8902703175, 'White', 'Walter', 'Albuquerque 123')
agregar_ta(tabla, hash_guia, dato, 'numero')
dato = Guia(845854384, 'Goodman', 'Saul', 'Albuquerque 572')
agregar_ta(tabla, hash_guia, dato, 'numero')
dato = Guia(6862011508, 'Jessie', 'Pinkman', 'Albuquerque 1528')
agregar_ta(tabla, hash_guia, dato, 'numero')
dato = Guia(6422714967, 'Ehrmantraut', 'Mike', 'Albuquerque 741')
agregar_ta(tabla, hash_guia, dato, 'numero')
dato = Guia(7660453450, 'Schrader', 'Hank', 'Nuevo Mexico 1068')
agregar_ta(tabla, hash_guia, dato, 'numero')

barrido_ta(tabla)
'''

#Ej 5


class Contacto(object):
    def __init__ (self, apellido, nombre, correo):
        self.apellido = apellido
        self.nombre = nombre
        self.correo = correo
    
    def __str__ (self):
        return self.apellido + " " + self.nombre + ": " + self.correo

tabla = crear_tabla(20)

dato = Contacto('White', 'Walter', 'Heisenberg@gmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Goodman', 'Saul', 'SGoodman@hotmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Jessie', 'Pinkman', 'Vatoloco@gmail.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Ehrmantraut', 'Mike', 'MikeEr@outlook.com')
agregar_tc(tabla, bernstein_contactos, dato)
dato = Contacto('Schrader', 'Hank', 'AgenteHank@dea.com')
agregar_tc(tabla, bernstein_contactos, dato)

barrido_tc(tabla)










