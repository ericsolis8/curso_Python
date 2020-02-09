'''
def funcion(os = "Debian"):
    print("Sistema operativo: "+os)

funcion()
funcion("Mac")
funcion("Windows")
funcion("Linux")
'''

'''
#lista como parametro
def funcion(nombres):
    for x in nombres:
        print(x)

nombres = ["heriberto","ezequiel","javier"]
funcion(nombres)
'''
'''
#return
def funcion(x):
    return 5 * x
print(funcion(3))
print(funcion(6))
print(funcion(9))
'''
#argumentos clave valor
def funcion(niño1, niño2, niño3):
    print("El mas joven es "+ niño2)
funcion(niño1="jhon", niño2="dewey", niño3="tom")
