'''
Un diccionario es una coleccion desordenada, modificable e indexada.
En python se escriben entre llaves y tienen CLAVES Y VALORES.
'''
diccionario = {
    "Marca": "Ford",
    "Modelo": "Mustang",
    "Año": 1964
}
'''
print(diccionario) #imprime el diccionario
diccionario["Año"]=2019 #cambiar valor de año
'''
'''
#recorrer el diccionario | funcion items() | values()
for x, y in diccionario.items():
    print(x, y)
'''
'''
#Validar si una CLAVE existe en el diccionario
if "Modelo" in diccionario:
    print("Si, 'Modelo' is una clave en este diccionario")
'''
#contador print(len(diccionario))
'''
#agregar elementos
diccionario["Color"] = "Negro"
print(diccionario)
'''
