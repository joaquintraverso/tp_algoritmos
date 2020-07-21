from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final
from tda_pila_dinamica import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice
import time
import os
from math import asin, sqrt, sin, cos, radians

#Ejercicio 1

'''
cola = Cola()
vocales = 'aeiouAEIOU'

while(tamanio(cola) < 10):
    x = randint(65, 122)
    arribo(cola, chr(x))

for i in range (tamanio(cola)):
    if (en_frente(cola) in vocales):
        atencion(cola)
    else:
        mover_final(cola)

print('cola sin vocales: ')
while(not cola_vacia(cola)):
    print(atencion(cola))
'''

#Ejercicio 2
'''
cola = Cola()
pila = Pila()

while tamanio(cola) < 10:
    x = input(print('ingrese un elemento a la cola: '))
    arribo(cola, x)

print('cola original')
while not cola_vacia(cola):
    x = atencion(cola)
    apilar(pila,x)
    print(x)

print('cola invertida')
while not pila_vacia(pila):
    x = desapilar(pila)
    arribo(cola,x)
    print(x)
'''

#Ejercicio 3
'''
cola = Cola()
pila = Pila()
aux = True

while tamanio(cola) < 5:
    x = input(print('ingrese un elemento a la cola: '))
    arribo(cola, x)

for i in range (tamanio(cola)):
    x = en_frente(cola)
    apilar(pila,x)
    mover_final(cola)

while not cola_vacia(cola):
    x = atencion(cola)
    x1 = desapilar(pila)
    if (x != x1):
        aux = False

if (aux == True):
    print('es un palindromo')
else:
    print('no es un palindromo')
'''

#Ejercicio 4

'''
cola = Cola()

while(tamanio(cola) < 10):
    arribo(cola, randint(0, 100))

for i in range(1,tamanio(cola)):
    if en_frente(cola) <= 3:
        mover_final(cola)
    else:
        div = 2
        while div < en_frente(cola):
            if en_frente(cola) % div == 0:
                atencion(cola)
            div += 1
        mover_final(cola)

print('cola de numeros primos: ')
while not cola_vacia(cola):
    print(atencion(cola))
'''

#Ejercicio 5
'''
cola = Cola()
pila = Pila()

while tamanio(pila) < 3:
    apilar(pila,randint(0, 100))

print('pila normal:')
while not pila_vacia(pila):
    x = desapilar(pila)
    arribo(cola,x)
    print(x)

while not cola_vacia(cola):
    apilar(pila,atencion(cola))

print('pila invertida:')
while not pila_vacia(pila):
    print(desapilar(pila))

'''

#Ejercicio 6
'''
cola = Cola()

while(tamanio(cola) < 20):
    arribo(cola, randint(0, 10))

cont = 0
buscado = int(input('ingrese elemento a buscar: '))

while not cola_vacia(cola):
    if buscado == atencion(cola):
        cont += 1

print('el elemento ', buscado,' se encontro ', cont,' veces')

'''

#Ejercicio 7

'''
cola = Cola()

while(tamanio(cola) < 5):
    arribo(cola, randint(0, 100))

print('cola original:')
for i in range(tamanio(cola)):
    print(en_frente(cola))
    mover_final(cola)

buscado = int(input('ingrese la posicion a eliminar: '))

for i in range(tamanio(cola)):
    if i == buscado-1:
        atencion(cola)
    else:
        mover_final(cola)

print('cola modificada:')
while not cola_vacia(cola):
    print(atencion(cola))

'''

#Ejercicio 8
'''
cola = Cola()
cola_aux = Cola()

numero = int(input('ingrese un numero: '))

while numero != 0:
    while not cola_vacia(cola) and en_frente(cola) <= numero:
        arribo(cola_aux, atencion(cola))
    arribo(cola_aux,numero)
    while not cola_vacia(cola):
        arribo(cola_aux, atencion(cola))
    while not cola_vacia(cola_aux):
        arribo(cola,atencion(cola_aux))

    numero = int(input('ingrese un numero: '))


print('cola ordenada:')
while not cola_vacia(cola):
    print(atencion(cola))
'''

#Ejercicio 9

#Formula rango: R= Max - Min

'''
cola = Cola()

while(tamanio(cola) < 5):
    arribo(cola, randint(-100, 100))

max = en_frente(cola)
min = en_frente(cola)
cont_neg = 0

print('cola: ')
for i in range(tamanio(cola)):
    print(en_frente(cola))
    mover_final(cola)

while not cola_vacia(cola):
    x = atencion(cola)
    if min > x:
        min = x
    if max < x:
        max = x
    if x < 0:
        cont_neg += 1

print('El rango es: ', (max - min), '\nCantidad de numeros negativos: ', cont_neg)
'''

#Ejercicio 10

'''
dato = ['','']
cola_aux = Cola()
cola_personajes = Cola()
cola_personajes2 = Cola()

archivo = open('personajes')

linea = archivo.readline()

while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    arribo(cola_personajes, linea)
    linea = archivo.readline()

while not cola_vacia(cola_personajes):
    x = atencion(cola_personajes)
    if x[1] == 'Alderaan' or x[1] == 'Endor' or x[1] == 'Tatooine':
        arribo(cola_aux,x)

    if x[0] == 'Luke Skywalker' or x[0] == 'Han Solo':
        print('El planeta natal de', x[0], 'es', x[1])
    
    if x[0] != 'Yoda': 
        arribo(cola_personajes2,x)
    else:
        #ingresa el personaje antes que Yoda
        print('Personaje nuevo')
        dato[0] = input('Nombre: ')
        dato[1] = input('Planeta: ')
        arribo(cola_personajes2,dato)
        arribo(cola_personajes2,x)
    
    if x[0] == 'Jar Jar Binks':
        atencion(cola_personajes)

print('Personajes que son de Alderaan, Endor o Tatooine: ')
while not cola_vacia(cola_aux):
    print(atencion(cola_aux))    

print('Cola modificada: ')
while not cola_vacia(cola_personajes2):
    print(atencion(cola_personajes2))
'''

#Ejercicio 11

'''
cola1 = Cola()
cola2 = Cola()

print('Ingrese numeros ordenados de manera creciente para cola1: ')
num = int(input('Numero: '))
while num != 0:
    arribo(cola1, num)
    num = int(input('Numero: '))

print('Ingrese numeros ordenados de manera creciente para cola2: ')
num = int(input('Numero: '))
while num != 0:
    arribo(cola2, num)
    num = int(input('Numero: '))

for i in range(tamanio(cola1)):
    if en_frente(cola1) < en_frente(cola2):
        mover_final(cola1)
    else:
        while en_frente(cola1) > en_frente(cola2):
                arribo(cola1, atencion(cola2))
        mover_final(cola1)

while not cola_vacia(cola2):
    arribo(cola1, atencion(cola2))

print('Cola ordenada: ')
while not cola_vacia(cola1):
    print(atencion(cola1))
'''

#Ejercicio 12

'''
cola = Cola()
cola_digitos = Cola()
digitos = '1234567890'
letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
cont = 0
aux_1 = False
aux_2 = False

while(tamanio(cola) < 30):
    arribo(cola, chr(randint(0, 255)))

for i in range(tamanio(cola)):
    x = en_frente(cola)
    if x in digitos:
        arribo(cola_digitos,atencion(cola))
    else:
        mover_final(cola)
    if x == '?':
        aux_1 = True
    if x == '#':
        aux_2 = True

for i in range(tamanio(cola)):
    x = en_frente(cola)
    if x.upper() in letras:
        cont += 1
    mover_final(cola)

if aux_1 == True:
    print('El caracter "?" existe')
else:
    print('El caracter "?" no existe')

if aux_2 == True:
    print('El caracter "#" existe')
else:
    print('El caracter "#" no existe')

print('Cantidad de letras en la segunda cola: ', cont)
'''

#Ejercicio 13

'''
cola1 = Cola()
cola2 = Cola()
cola3 = Cola()

semaforo1 = ['Verde','Amarillo','Rojo']
semaforo2 = ['Rojo','Verde','Amarillo']
semaforo3 = ['Amarillo','Rojo','Verde']

for i in range(0,2):
    arribo(cola1,semaforo1[i])
    arribo(cola2,semaforo2[i])
    arribo(cola3,semaforo3[i])

for i in range(0,5):
    print('semaforo 1:', en_frente(cola1))
    print('semaforo 2:', en_frente(cola2))
    print('semaforo 3:', en_frente(cola3))

    time.sleep(5)
    os.system('cls')

    mover_final(cola1)
    mover_final(cola2)
    mover_final(cola3)
'''

#Ejercicio 14

cola = Cola()
cola_aux = Cola()
actual = [15.065, 68.764]

archivo = open('bases rebeldes')

linea = archivo.readline()

while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = linea[1].title()
    arribo(cola, linea)
    linea = archivo.readline()

min_dato = ['', 0, 0]
flota = 0
flota_dato = ['', 0, 0]
a1 = radians(actual[0])
a2 = radians(actual[1])
r = 6371000

print('coordenadas actuales: ', a1, a2)

print('\nbases rebeldes: ')
for i in range(tamanio(cola)):
    x = atencion(cola)
    x[2] = radians(float(x[2]))
    x[3] = radians(float(x[3]))
    print(x)
    arribo(cola,x)

while not cola_vacia(cola):
    x = atencion(cola)
    b1 = radians(x[2])
    b2 = radians(x[3])
    haversine = 2*r*asin(sqrt(sin((a1-a2)/2)**2+cos(a1)*cos(a2)*sin((b1-b2)/2)**2))
    haversine = int(haversine)
   # if min == 0: #error
   #     min = haversine
   #    min_dato = [x[0], haversine, x[1]]
   #if min > haversine:
   #     min_dato = [x[0], haversine, x[1]]
    if flota < int(x[1]):
        flota_dato = [x[0], haversine, x[1]]
    arribo(cola_aux, [x[0], haversine, x[1]])

print('\nBase con mayor flota: ', flota_dato)
#print('\nBase mas cercana a la posicion actual: ', min_dato)

#Ejercicio 15
 

