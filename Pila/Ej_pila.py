#from tda_pila import Pila, pila_llena, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice
from tda_pila_dinamica import Pila, pila_vacia, desapilar, apilar, tamanio, cima

pila = Pila()
pila_aux = Pila()

'''
while(not pila_llena(pila)):
    apilar(pila, randint(0,100))

#Ejercicio 1 

def ocurrencias(pila, bus):
    cont = 0
    print('Pila: ')
    while (not pila_vacia(pila)):
        if (cima(pila) == bus):
            cont = cont + 1
        aux = desapilar(pila)
        print(aux)
    return print('El objeto que se repitio ', cont , 'veces.')

buscado = int(input('Ingrese el numero a buscar dentro de la pila: '))
print(ocurrencias(pila, buscado))
'''

#Ejercicio 2

'''
    print("pila normal")
    while(not pila_vacia(pila)):
        x = desapilar(pila)
        if ((x % 2) == 0):
            apilar(pila_aux, x)
        print(x)

    while(not pila_vacia(pila_aux)):
        aux = desapilar(pila_aux)
        apilar(pila, aux)

    print("pila par")
    while(not pila_vacia(pila)):
        print(desapilar(pila))
'''

#Ejercicio 3

'''
ocurrencia = int(input('Ingrese la ocurrencia a cambiar: '))
nueva_ocurrencia = int(input('Ingrese el nuevo numero: '))

while (not pila_vacia(pila)):
    x = desapilar(pila)
    if (x == ocurrencia):
        apilar(pila_aux, nueva_ocurrencia)
    else:
        apilar(pila_aux, x)
        
#Acomodo la pila
while(not pila_vacia(pila_aux)):
    aux = desapilar(pila_aux)
    apilar(pila, aux)

print ('Pila modificada: ')

while(not pila_vacia(pila)):
    print(desapilar(pila))
'''

#Ejercicio 4

'''
while(not pila_llena(pila)):
    apilar(pila, randint(0, 100))

print("pila normal")
while(not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux, x)
    print(x)

pila = pila_aux

print("pila invertida")
while(not pila_vacia(pila)):
    print(desapilar(pila))
'''

#Ejercicio 5

'''
palabra = input('ingrese una palabra: ')

for I in range(0,len(palabra)):
    apilar(pila,palabra[I])

controlador = True

for I in range(0,len(palabra)):
    x = desapilar(pila)
    if (x != palabra[I]):
        controlador = False

if(controlador == True):
    print('La palabra es un palindromo')
else:
    print('La palabra no es un palindromo')
'''

#Ejercicio 6

'''
palabra = input('ingrese una palabra: ')
x = ''

for I in range(0,len(palabra)):
    apilar(pila,palabra[I])

while(not pila_vacia(pila)):
    x = (x + desapilar(pila))

print('palabra invertida: ', x)
'''

#Ejercicio 7

'''
while(not pila_llena(pila)):
    apilar(pila, randint(0,100))

elemento = int(input('ingrese el elemento a eliminar: '))

while (not pila_vacia(pila)):
    x1 = tamanio(pila)
    x = desapilar(pila)
    if (x1 != elemento):
        apilar(pila_aux, x)

while(not pila_vacia(pila_aux)):
    x = desapilar(pila_aux)
    apilar(pila, x)

print('pila modificada:')
while(not pila_vacia(pila)):
    print(desapilar(pila))
'''

#Ejercicio 8

'''
pila = Pila()
pilaaux = Pila()
pilapar = Pila()
pilaimpar = Pila()
mazo = Pila()
mazo_espada = Pila()
mazo_oro = Pila()
mazo_copa = Pila()
mazo_basto = Pila()

palos = ['espada', 'basto', 'copa', 'oro']

while(tamanio(mazo)<40):
    dato = ['', 0]
    dato[0] = choice(palos)
    dato[1] = randint(1, 12)
    apilar(mazo, dato)

while(not pila_vacia(mazo)):
    x = desapilar(mazo)
    if (x[0] == 'espada'):
        apilar(mazo_espada, x)
    elif (x[0] == 'copa'):
        apilar(mazo_copa, x)
    elif (x[0] == 'oro'):
        apilar(mazo_oro, x)
    else:
        apilar(mazo_basto, x)
'''

#Ejercicio 9

'''
num = int(input('ingrese un numero: '))
resultado = 1
apilar(pila,resultado)

while(num > 0):
    resultado = desapilar(pila)
    resultado = resultado * num
    apilar(pila,resultado)
    num -= 1

print('el resultado es= ', resultado)
'''

#Ejercicio 10
'''
for I in range(0,4):
    x = input('ingrese un nombre: ')
    apilar(pila,x)

x = 'atenea'
x1 = desapilar(pila)

apilar(pila,x)
apilar(pila,x1)

while(not pila_vacia(pila)):
    print(desapilar(pila))
'''

#Ejercicio 11
'''
while(not pila_llena(pila)):
    x = randint(97, 122)
    apilar(pila,chr(x))

contador = 0

while(not pila_vacia(pila)):
    x = desapilar(pila)
    print(x)
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        contador += 1

print('cantidad de vocales: ', contador)
'''

#Ejercicio 12
'''

while(not pila_llena(pila)):
    x = input(print ('ingrese un personaje: '))
    apilar(pila,x)

while(not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux,x)
    if((x == 'Leia Organa') or (x == 'Boba Fett')):
        print('el personaje', x,'se encuentra en la pila')

while(not pila_vacia(pila_aux)):
    apilar(pila,desapilar(pila_aux))

print('personajes: ')
while(not pila_vacia(pila)):
    print(desapilar(pila))

'''

#Ejercicio 13
'''
numero = int(input('ingrese un numero '))
while numero != 0:
    if(pila_vacia(pila)):
        apilar(pila, numero)
    else:
        if(cima(pila) <= numero):
            apilar(pila, numero)
        else:
            while(not pila_vacia(pila) and cima(pila) > numero):
                daux = desapilar(pila)
                apilar(pila_aux, daux)
            apilar(pila, numero)
            while(not pila_vacia(pila_aux)):
                daux = desapilar(pila_aux)
                apilar(pila, daux)

    numero = int(input('ingrese un numero '))

print('pila ordenada')
while (not pila_vacia(pila)):
    print(desapilar(pila))

'''

#Ejercicio 14

'''
while(not pila_llena(pila)):
    apilar(pila,randint(0,100))

def quicksort(vector, primero, ultimo):
    apilar(pila,[primero, ultimo])
    while(not pila_vacia(pila)):
        dato = desapilar(pila)
        primero = dato[0]
        ultimo = dato[1]
        if(primero<ultimo):
            pivot = ultimo
            izq = primero
            der = ultimo-1
            while(izq < der):
                while(vector[izq] < vector[pivot]):
                    izq += 1
                
                while(vector[der] > vector[pivot]):
                    der -= 1

                if(izq < der):
                    vector[izq], vector[der] = vector[der], vector[izq]

            if(vector[izq]>vector[pivot]):
                vector[izq], vector[pivot] = vector[pivot], vector[izq]

            apilar(pila,[primero, izq-1])#quicksort(vector, primero, izq-1)
            apilar(pila,[izq+1, ultimo])#quicksort(vector, izq+1, ultimo)
'''

#Ejercicio 15
'''
pila_V = Pila()
pila_VII = Pila()

print('The empire strikes back')
while(not pila_llena(pila_V)):
    x = input(print('ingrese el personaje: '))
    apilar(pila_V,x)
print('The force awakens')

while(not pila_llena(pila_VII)):
    x = input(print('ingrese el personaje: '))
    apilar(pila_VII,x)

while not(pila_vacia(pila_V)):
    x = desapilar(pila_V)
    while not(pila_vacia(pila_VII)):
        x1 = desapilar(pila_VII)
        apilar(pila,x1)
        if(x == x1):
            apilar(pila_aux,x)
    while(not pila_vacia(pila)):
        x = desapilar(pila)
        apilar(pila_VII,x)

print('personajes de ambos ep: ')
while(not pila_vacia(pila_aux)):
    print(desapilar(pila_aux))
'''

#####################################################
##################TDA_PILA_DINAMICA##################
#####################################################

#Ejercicio 16
'''

voc = 0
cons = 0
caracter = 0
espacios = 0
porcentaje = 0
cant_num = 0
z = 0

vocal = 'aeiouAEIOU'
letras = 'bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ'
cart = '.,-_!"?¿/()*+%$#@°='
numeros = '1234567890'

parrafo = input(print('ingresar un parrafo (finalizar con un .): '))

while (tamanio(pila) < len(parrafo)):
        for i in range(0, len(parrafo)):
            apilar(pila,parrafo[i])

while (not pila_vacia(pila)):
    x = desapilar(pila)
   
    if (x in vocal):
        voc += 1
   
    elif (x == ' '):
        espacios += 1
        
    elif(x in cart):
        caracter += 1
        if (x in numeros):
            cant_num += 1

    elif (x in letras):
        cons += 1
        if (x == 'z'):
            z += 1

porcentaje = (voc / cons) * 100

print('cantidad de vocales: ',voc)
print('cantidad de caracteres: ',caracter)
print('cantidad de consonantes: ',cons)
print('cantidad de numeros: ', cant_num)
print('cantidad de espacios: ', espacios)

print('porcentaje de vocales sobre consonantes: ',porcentaje, '%')

if (voc == cons):
    print('cantidad de vocales igual a la de consonantes')

if (voc == caracter):
    print('cantidad de vocales igual a la de caracteres')

if (z > 0):
    print('en el parrafo existe la z')
'''

#Ejercicio 17

'''
dato = [0,'']

dato[0] = float(input(print('ingrese el peso: ')))

while dato[0] != 0:
    dato[1] = input(print('ingrese el nombre objeto: '))
    
    if(pila_vacia(pila)):
        apilar(pila, dato)
    else:
        if (cima(pila) <= dato):
            apilar(pila, dato)
        else:
            while(not pila_vacia(pila) and cima(pila) > dato):
                daux = desapilar(pila)
                apilar(pila_aux, daux)
            apilar(pila, dato)
            while(not pila_vacia(pila_aux)):
                daux = desapilar(pila_aux)
                apilar(pila, daux)
    
    dato = [0,'']
    dato[0] = float(input(print('ingrese el peso: ')))
    
print('pila ordenada:')
while not pila_vacia(pila):
    print(desapilar(pila))
'''

#Ejercicio 18

'''
pila_peliculas = Pila()
pila_marvel = Pila()
pila_2014 = Pila()
cont_2018 = 0

titulo = input('titulo: ')
while titulo != '':
    anio = int(input('año: '))
    estudio = input('estudio cinematografico: ')
        
    apilar(pila_peliculas,[titulo, anio, estudio])

    titulo = input('titulo: ')

while not pila_vacia(pila_peliculas):
    dato = desapilar(pila_peliculas)
    if str(dato[1]) == '2014':
        apilar(pila_2014,dato)
    elif str(dato[1]) == '2018':
        cont_2018 += 1
    elif str(dato[1]) == '2016' and dato[2] == 'Marvel Studios':
        apilar(pila_marvel,dato)
    
print('cantidad de peliculas estrenadas en 2018: ', cont_2018)

print('peliculas estrenadas en 2014: ')
while not pila_vacia(pila_2014):
    x = desapilar(pila_2014)
    print(x[0])

print('peliculas estrenadas en 2016 por Marvel Studios: ')
while not pila_vacia(pila_marvel):
    x = desapilar(pila_marvel) 
    print(x[0])
'''

#Ejercicio 19
'''
cond = 'y'
cont_pasos = 0
movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'noroeste', 'sureste', 'suroeste']

while (cond == 'y'):
    apilar(pila, choice(movimientos))
    cont_pasos += 1 
    cond = input('presione "y" para continuar cargando: ')

print('pasos realizados: ')
while not pila_vacia(pila):
    x = desapilar(pila)
    apilar(pila_aux,x)
    print(x)

while not pila_vacia(pila_aux):
    apilar(pila,desapilar(pila_aux))

while not pila_vacia(pila):
    x = desapilar(pila)
    if x == 'norte':
        apilar(pila_aux, 'sur')
    elif x == 'sur':
        apilar(pila_aux, 'norte')
    elif x == 'este':
        apilar(pila_aux, 'oeste')
    elif x == 'oeste':
        apilar(pila_aux, 'este')
    elif x == 'norte':
        apilar(pila_aux, 'sur')
    elif x == 'noreste':
        apilar(pila_aux, 'suroeste')
    elif x == 'noroeste':
        apilar(pila_aux, 'sureste')
    elif x == 'sureste':
        apilar(pila_aux, 'noroeste')
    elif x == 'suroeste':
        apilar(pila_aux, 'noreste')

while not pila_vacia(pila_aux):
    apilar(pila,desapilar(pila_aux))

print('pasos realizados para volver al punto de partida:')
while not pila_vacia(pila):
    print(desapilar(pila))

print('el robot realiza una cantidad de ', cont_pasos,' pasos de ida')
print('el robot realiza en total ', cont_pasos*2,' de pasos en ida y vuelta')
'''

#Ejercicio 20

'''
def fibonacci(numero, pila):
    if numero == 1: 
        return 0
    elif numero == 2: 
        return 1
    else:
        numero -= 2
        apilar(pila, 0)
        apilar(pila, 1)
        while numero > 0:
            #sacamos el ultimo
            cim = desapilar(pila)
            #tambien sacamos el anteultimo
            cim_2 = desapilar(pila)
            #calculamos el actual
            n_actual = cim + cim_2 
            
            #metemos los 3
            apilar(pila, cim_2) 
            apilar(pila, cim)
            apilar(pila, n_actual)
            
            numero -= 1
        return cima(pila)
print(fibonacci(8, pila))
'''

#Ejercicio 21 

'''
abril = Pila()
pila_aux = Pila()

cant = 0
prom = 0
max = 0
min = 40

while (tamanio(abril) < 6):
    cant += 1
    dato = randint(0,30)
    apilar(abril,dato)

while not pila_vacia(abril):
    x = desapilar(abril)
    apilar (pila_aux, x)
    if (max < x):
        max = x
    if (min > x):
        min = x
    prom += x

prom = prom / cant
encima = 0
debajo = 0

while not pila_vacia(pila_aux):
    y = desapilar(pila_aux)
    apilar(abril, y)
    if (prom < y):
        encima += 1
    else:
        debajo += 1

print ('Minima: ' ,min)
print ('Maxima: ' ,max)
print ('Promedio temperatura: ' ,prom)
print ('Dias por debajo de la media: ' ,debajo)
print ('Dias por Encima: ' ,encima)
print ('Pila real')

while not pila_vacia(abril):
    print(desapilar(abril))

'''

#Ejercicio 22

'''
personajes = Pila()

personajes = ['Groot' , 'Magneto' , 'Iron Man' , 'Rocket Raccoon' , 'Sam' ,'Black Widow' , 'Bruce Banner']

lista = Pila()

while (tamanio(lista)) < 7:
    dato = ['',0]
    dato[0] = choice(personajes)
    dato[1] = randint(1,10)
    apilar(lista,dato)

def personajes_marvel(pila_personajes):
    i = 1
    while (not (pila_vacia(pila_personajes))):
        personaje = desapilar(pila_personajes)
        if (personaje[0] == 'Rocket Raccoon' or personaje[0] == 'Groot'):
            print(personaje[0], 'esta en la posición', i+1)
        if (personaje[1] > 5):
            print(personaje[0], 'participo en mas de 5 peliculas')
        if (personaje[0] == 'Black Widow'):
            print(personaje[0], 'participo en', personaje[1], 'peliculas')
        if (personaje[0][0] in ['C','D','G']):
            print ('comienza con C, D o G: ',personaje[0])
        i += 1
    return

print(personajes_marvel(lista))
'''