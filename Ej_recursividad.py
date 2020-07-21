#ej1

def fibonacci(numero):
    if(numero==0 or numero==1):
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

#print(fibonacci(10))

#ej2

def suma(numero):
    if(numero==0):
        return numero
    else:
        return numero + suma(numero-1)

#print(suma(22))

#ej4

def potencia(base,exp):
    if (exp==0):
        return 1
    elif (base == 0):
        return 0
    elif (exp == 1):
        return base
    else:
        return base * potencia(base,exp - 1)

#print(potencia(2,4))

#ej5

def inv_palabra(palabra,long):
    if(long == 0):
        return ""
    else:
        return palabra[long-1] + inv_palabra(palabra,long-1)

#palabra='hola'
#print(inv_palabra(palabra,len(palabra)))

#ej7

def binario(numero):
    if(numero <= 1):
        return str(numero)
    else:
        return binario(numero//2) + str(numero % 2)

#print(binario(1))

#ej8

def logaritmo(base,numero):
    if(base == numero):
        return 1
    else:
        return 1 + logaritmo(base,numero/base)

#ej9

def digitos(num,con):
    if(num<10):
        return con+1
    else:
        return digitos(num//10,con+1)

#print(digitos(1,0))

#ej10

def inv_num(num):
    pos= digitos(num,0)
    pos=pos-1
    if (num<10):
        return num
    else:
        return (num%10)*potencia(10,pos)+inv_num(num//10)

#print(inv_num(123))

#ej11

def mcd(m, num):
    if(m % num == 0):
        return num
    else:
        return mcd(num, m % num)


#ej12

def mcm(m, num):
    if(num % m == 0):
        return num
    else:
        return mcm(num, m * num)

#ej13

def suma_elementos(numero):
    if(numero<10):
        return numero
    else:
        return suma_elementos(numero//10)+(numero%10)

#print(suma_elementos(333))

#ej14

def raiz_2(num,x):
    if ((x * x) == num):
        return x
    elif ((x*x) > 1):
        return x-1
    else:
        return raiz_2 (num,x+1)

#ej15

def prog_geometrica(num):
    if(num == 1):
        return 2
    else:
        return -3 * prog_geometrica(num-1)

#ej16

def vec_invertido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        vec_invertido(vec[0:-1])

vec = [1,2,3,4]

#print(vec_invertido(vector))

#ej17

def rec_matriz(mat, i, j):
    if (i < len(mat)) and (j < len(mat[i])):
        print(mat[i][j])
        if(j == len(mat[i])-1):
            i+=1
            j=0
        rec_matriz(mat,i,j+1)

mat = [[1,2,3],[1,2,3],[1,2,3]]

#print(rec_matriz(matriz,0,0))

#ej18

def sucesion(num):
    if (num == 1):
        return 2
    else:
        return ((num + 1) / sucesion(num - 1))

#print(sucesion(num))


#ej19 

def bus_centinela (bus,v,i):
    if (bus == v[i]):
        print('posicion del elemento: ', i)
    else:
        i+=1
        return bus_centinela(bus,v,i)

vec = [0,9,6,4,32,5,7,1,10]

#print(bus_centinela(5,vec,0))

#ej 20

def bus_bin(bus,v,pri,ult):
    if (pri > ult):
        print("No se encuentra el elemento buscado")
    med = (pri + ult) // 2
    if (bus == v[med]):
        print("El elemento se encuentra en la posicion ",med)
    elif (bus > v[med]):
        return bus_bin(bus,v,med+1,ult)
    else:
        return bus_bin(bus,v,pri,med-1)

vector = [0,1,2,3,4,5,6,7,8,9,10]

#print(bus_bin(7,vector,0,len(vector)-1))

#ej24

def sucesion2 (num):
    if(num == 1):
        return 5.25
    else:
        return sucesion2(num-1) * 4


#ej25

def sucesion3 (num):
    if (num == 1):
        return 3
    elif (num >= 2):
         return sucesion3 ( num - 1 ) + 2 * num
