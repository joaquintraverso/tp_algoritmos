from tda_lista import nodoLista, Lista, insertar, eliminar, busqueda, barrido, tamanio, lista_vacia, criterio, barrido_con_sublista
from random import randint, choice
from datetime import time, date

#Ej 1

'''
lista = Lista()

for i in range (10):
    insertar(lista, randint(0,20,))

c = 0
aux = lista.inicio
while aux is not None:
    aux = aux.sig
    c += 1

print(c)
'''

#Ej 2

'''
lista = Lista()
vocales = 'aeiouAEIOU'

for i in range(5):
    insertar(lista, chr(randint(65,122)))

print('lista normal: ')
barrido(lista)

aux = lista.inicio

for i in range(tamanio(lista)):
    if aux.info in vocales:
        eliminar(lista, aux.info)
    aux = aux.sig

print('lista sin vocales: ')
barrido(lista)
'''

#Ej 3

'''
lista = Lista()
lista_imp = Lista()

for i in range (5):
    insertar(lista, randint(0,20))

print('lista normal: ')
barrido(lista)

aux = lista.inicio

while aux is not None:
    if (aux.info % 2 != 0):
        eliminar(lista, aux.info)
        insertar(lista_imp, aux.info)
    aux = aux.sig
    
print('\nlista par: ')
barrido(lista)

print('\nlista impar: ')
barrido(lista_imp)
'''

#Ej 6

'''
lista = Lista()

dato = ['', '', '', '']
dc = 0
marvel = 0

archivo = open('personajes')

linea = archivo.readline()

while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    insertar(lista, linea)
    linea = archivo.readline()

print('lista personajes: ')
barrido(lista)

print('')

aux = lista.inicio

while aux is not None:
    dato = aux.info
    if dato[0] == 'Linterna Verde':
        eliminar(lista, aux.info)
        print('Se elimino el nodo de Linterna Verde')
    if dato[0] == 'Wolverine':
        print('Wolverine hizo su primer aparicion en el año', dato[2])
    if dato[0] == 'Dr. Strange':
        dato[1] = 'Marvel'
        print('Se cambio la casa de Dr. Strange a Marvel')
    if 'Traje' in dato[3] or 'Armadura' in dato[3]:
        print('La biografia del personaje', dato[0], 'contiene la palabra Traje o Armadura')
    if int(dato[2]) <= 1963:
        print('El personaje', dato[0], 'de la casa', dato[1], 'hizo su aparicion antes del 1963')
    if dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla':
        print('El personaje', dato[0], 'pertenece a la casa', dato[1])
    if dato[1] == ' Marvel':
        marvel += 1
    else:
        dc += 1
    aux = aux.sig

print('La casa Marvel tiene la cantidad de comics de: ', marvel)
print('La casa DC tiene la cantidad de comics de: ', dc)
'''

#Ej 9

'''
class Alumno(object):

    def __init__(self, apellido, nombre, legajo):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo

    def __str__(self):
        return self.apellido + " " + self.nombre + " | " + str(self.legajo)

class Parcial(object):

    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return self.materia + " " + str(self.nota) + " " + str(self.fecha)

lista = Lista()

dato = Alumno('Martinez', 'Gonzalo', 35)
insertar(lista, dato, 'apellido')
dato = Alumno('Falcao', 'Radamel', 48)
insertar(lista, dato, 'apellido')
dato = Alumno('Funes Mori', 'Ramiro', 21)
insertar(lista, dato, 'apellido')

dato = Parcial('Ataque', 8.3, date(2018, 12, 9))
pos = busqueda(lista, 35, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Pase', 7.9, date(2019, 9, 25))
pos = busqueda(lista, 35, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Remate', 6.5, date(2020, 9, 12))
pos = busqueda(lista, 35, 'legajo')
insertar(pos.sublista, dato, 'materia')

dato = Parcial('Ataque', 8.7, date(2020, 12, 9))
pos = busqueda(lista, 48, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Remate', 8, date(2019, 9, 25))
pos = busqueda(lista, 48, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Salto', 9, date(2020, 7, 13))
pos = busqueda(lista, 48, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Resistencia', 5.5, date(2019, 5, 16))
pos = busqueda(lista, 48, 'legajo')
insertar(pos.sublista, dato, 'materia')

dato = Parcial('Defensa', 9.1, date(2020, 12, 9))
pos = busqueda(lista, 21, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Salto', 8.5, date(2020, 7, 13))
pos = busqueda(lista, 21, 'legajo')
insertar(pos.sublista, dato, 'materia')
dato = Parcial('Resistencia', 9.3, date(2019, 5, 16))
pos = busqueda(lista, 21, 'legajo')
insertar(pos.sublista, dato, 'materia')

print('lista de jugadores: ')
barrido(lista)

aux = lista.inicio

while aux is not None:
    print('\n')
    sub = aux.sublista.inicio
    promedio = 0
    notas = True
    while sub is not None:
        if sub.info.nota < 6:
            notas = False
        promedio = promedio + sub.info.nota 
        sub = sub.sig
    if notas and tamanio(aux.sublista) > 0:
        print(aux.info, 'no desaprobo ningun parcial')
    promedio = promedio/tamanio(aux.sublista)
    if(tamanio(aux.sublista) > 0 ):
        print('El promedio de notas de', aux.info, 'es de:', str(promedio))
    if promedio > 8.89:
        print(aux.info, 'tiene un promedio mayor a 8,89')
    if aux.info.apellido[0] == 'L':
        print(aux.info, 'es L su letra inicial en el apellido')
        barrido(aux.sublista)
    aux = aux.sig 

'''

#Ej 11
'''

lista = Lista()

class personaje():

    def __init__(self, nombre, altura, edad, genero, especie, origen, episodio):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.origen = origen
        self.episodio = episodio

    def __str__(self):
        return self.nombre + ' / ' + str(self.altura) + ' / ' + str(self.edad) + ' / ' + self.genero + ' / ' + self.especie  + ' / ' + self.origen + ' / ' + str(self.episodio)

datos = personaje('Han Solo', 1.85, 66, 'M', 'Humano', 'Corellia', [1, 2, 3, 4, 5, 6, 7, 8])
insertar(lista, datos, 'nombre')

datos = personaje('Darth Vader', 2.03, 37, 'M', 'Humano', 'Polis Massa', [3, 4, 5, 6])
insertar(lista, datos, 'nombre')

datos = personaje('R2D2', 1.09, 67, 'M', 'Droide', 'Naboo', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')

datos = personaje('Yoda', 0.66, 900, 'M', 'Yoda', 'Desconocido', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')

datos = personaje('Breha Organa', 1.63, 38, 'F', 'Humano', 'Alderaan', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')

datos = personaje('Rey Skywalker', 1.70, 20, 'F', 'Humano', 'Jakku', [7, 8, 9])
insertar(lista, datos, 'nombre')

datos = personaje('C3PO', 1.75, 54, 'M', 'Droide', 'Tatooine', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')

datos = personaje('Chewbacca', 2.30, 140, 'M', 'Wookiee', 'Kashyyyk', [1, 2, 3, 4, 5, 6, 7, 8, 9])
insertar(lista, datos, 'nombre')

print('nombre / altura / edad / genero / especie / orien / episodios')
barrido(lista)
print()

#a
aux = lista.inicio
while aux is not None:
    if aux.info.genero == 'F':
        print(aux.info.nombre, 'Es un personaje femenino')
    aux = aux.sig
print()

#b
aux = lista.inicio
while aux is not None:
    if aux.info.especie == 'Droide':
        for i in range(len(aux.info.episodio)):
           if aux.info.episodio[i] <= 6:
               x = True
        if x == True:
            print(aux.info.nombre, 'Aparece en los primeros 6 episodios')
    aux = aux.sig
print()

#c
aux = lista.inicio
while aux is not None:
    if aux.info.nombre == 'Han Solo' or aux.info.nombre == 'Darth Vader':
        print('nombre / altura / edad / genero / especie / orien / episodios')
        print(aux.info)
    aux = aux.sig
print()

#e
aux = lista.inicio
max = -1
while aux is not None:
    if aux.info.edad >= 850:
        print(aux.info.nombre, 'Tiene mas de 850 años')
        if aux.info.edad > max:
            max_info = aux.info
            max = aux.info.edad
    aux = aux.sig
print(max_info.nombre, 'Es el mayor con', max_info.edad, 'anios\n')

'''

#Ej 15
'''

lista = Lista()

class Entrenador():
    def __init__(self, nombre, torneos, ganadas, perdidas):
        self.nombre = nombre
        self.torneos = torneos
        self.ganadas = ganadas
        self.perdidas = perdidas

    def __str__(self):
        return '\n' + self.nombre + ' / ' + str(self.torneos) + ' / ' + str(self.ganadas) + ' / ' + str(self.perdidas)

class Pokemon():
    def __init__(self, pokemon, nivel, tipo, subtipo):
        self.pokemon = pokemon
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return self.pokemon + ' / ' + str(self.nivel) + ' / ' + self.tipo + ' / ' + self.subtipo

dato = Entrenador('Ladron', randint(0, 5), randint(25, 125), randint(0, 100))
insertar(lista, dato, 'nombre')

aux = Pokemon('Bulbasur', randint(1, 20), 'Planta', 'Veneno')
pos = busqueda(lista, 'Ladron', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

aux = Pokemon('Charizard', randint(1, 20), 'Fuego', 'Volador')
pos = busqueda(lista, 'Ladron', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

dato = Entrenador('Pensador', randint(0, 3), randint(50, 200), randint(0, 100))
insertar(lista, dato, 'nombre')

aux = Pokemon('Butterfree', randint(1, 20), 'Bicho', 'Volador')
pos = busqueda(lista, 'Pensador', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

aux = Pokemon('Squirtle', randint(1, 20), 'Agua', '-')
pos = busqueda(lista, 'Pensador', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

dato = Entrenador('Cientifico', randint(0, 8), randint(50, 200), randint(0, 100))
insertar(lista, dato, 'nombre')

aux = Pokemon('Charmeleon', randint(1, 20), 'Fuego', '-')
pos = busqueda(lista, 'Cientifico', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

aux = Pokemon('Zubat', randint(1, 20), 'Veneno', 'Volador')
pos = busqueda(lista, 'Cientifico', 'nombre')
insertar(pos.sublista, aux, 'pokemon')

#d
barrido_con_sublista(lista)

#a
buscado = input('\nIngrese el entrenador a buscar: ')
pos = busqueda(lista, buscado, 'nombre')
if pos is not None:
    print(pos.info.nombre, 'cuenta con la cantidad de pokemones de', tamanio(pos.sublista))
else:
    print('El entrenador no existe')
print()

#c
aux = lista.inicio
while aux is not None:
    if aux.info.torneos >= 3:
        print(aux.info.nombre, 'Gano mas de 3 torneos')
    aux = aux.sig
print()

#e
aux = lista.inicio
while aux is not None:
    total = aux.info.ganadas + aux.info.perdidas
    porcentaje = (aux.info.ganadas * 100) / total
    if porcentaje >= 79:
        print(aux.info.nombre, 'Tiene mas del 79% de batallas ganadas')
    aux = aux.sig
print()

#g
aux = lista.inicio
while aux is not None:
    sub = aux.sublista.inicio
    total = 0
    while sub is not None:
        total += sub.info.nivel
        sub = sub.sig
    print(aux.info.nombre, 'Tiene un promedio de nivel de sus pokemones de', total / tamanio(aux.sublista))
    aux = aux.sig

'''