'''
def imprime_ordenado(coleccion):
    try:
        coleccion.sort()
    except AttributeError:
        pass
    print (coleccion)

imprime_ordenado(set((1,3,2)))
'''
#Agregando excepciones
def filtro_nombre(nombre):
    try:
        nombre = nombre.encode('ascii')
    except UnicodeError, e:
        if nombre == 'Eric':
            print('OK, Eric')
        else:
            raise e
    return nombre
filtro_nombre('Eric')