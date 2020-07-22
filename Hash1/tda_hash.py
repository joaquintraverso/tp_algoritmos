from tda_lista import Lista, insertar, eliminar, busqueda, tamanio, barrido

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla


def agregar_tc(tabla, hash, dato):
    '''Agrega elementos a una tabla cerrada'''
    pos = hash(dato, tabla)
    if tabla[pos] is None:
        tabla[pos] = dato
    else:
        if pos == len(tabla)-1:
            pos = -1
        pos_aux = pos
        while tabla[pos+1] is not None and hash(tabla[pos+1], tabla) == pos_aux:
            pos += 1
            if pos == len(tabla)-1:
                pos = -1
        if tabla[pos+1] is None:
            tabla[pos+1] = dato
        else:
            print('hacer rehasing')


def agregar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato, criterio)


def quitar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return eliminar(tabla[posicion], dato.palabra, criterio)
    else:
        return None


def quitar_tc(tabla, hash, dato):
    dato = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion] == dato):
            dato = tabla[posicion]
            tabla[posicion] = None
            #! revisar si hay colision y realizar desplazamineto
        else:
            print('aplicar funcion colision seguir busco')
    return None


def buscar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        return busqueda(tabla[posicion], dato.palabra, criterio)
    else:
        return None


def buscar_tc(tabla, hash, dato):
    pos = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion].codigo == dato.codigo):
            pos = posicion
        else:
            print('aplicar funcion colision seguir busco')
            if(posicion == len(tabla)-1):
                posicion = -1
            #! completar
            posaux = posicion
            while(tabla[posicion+1] is not None and hash(tabla[posicion+1], tabla) == posaux):
                posicion += 1
                if(posicion == len(tabla)-1):
                    posicion = -1
                if(tabla[posicion].codigo == dato.codigo):
                    pos = posicion
                    break
    return pos


def barrido_ta(tabla):
    '''Muestra los elementos de una tabla abierta'''
    for indice in tabla:
        if indice is not None:
            barrido(indice)


def barrido_tc(tabla):
    '''Muestra los elementos de una tabla cerrada'''
    for indice in tabla:
        if indice is not None:
            print(indice)


def hash_division(clave, tabla):
    return clave % len(tabla)


def hash_division_troopers(trooper, tabla):
    return trooper.codigo % len(tabla)


def bernstein(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def bernstein_palabra(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena.palabra:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_troopers(trooper, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in trooper.legion:
        h = h * 33 + ord(caracter)
    return h % len(tabla)


def bernstein_catedra(dato, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in dato.codigo[4:]:
        h = h * 33 + ord(caracter)
    return h % len(tabla)

def cantidad_elementos_ta(tabla):
    cantidad = 0
    for elemento in tabla:
        if(elemento is not None):
            cantidad += tamanio(elemento)
    return cantidad
    #return sum(tamanio(lista) for lista in tabla if lista is not None)


def cantidad_elementos_tc(tabla):
    # cantidad = 0
    # for elemento in tabla:
    #     if(elemento is not None):
    #         cantidad += 1
    # return cantidad
    return len(tabla) - tabla.count(None)


def hash_diccionario(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)
    

def hash_cifrado(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)

def hash_guia(dato, tabla):
    return dato.numero % len(tabla)

def bernstein_contactos(cadena, tabla):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in (cadena.apellido + cadena.nombre):
        h = h * 33 + ord(caracter)
    return h % len(tabla)
