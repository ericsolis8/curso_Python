'''
datos = [0,0,0,0,0,0]
for i in range(1,7):
    datos[i-1] = int(input("Dime el numero {}:".format(i) ))
print ("Los datos al reves son: ")
for i in range(6,0,-1):
    print(datos[i-1])
'''
datos = []
for i in range(1,7):
    nuevoDato = int(input("Dime el numero {}: ".format(i)))
    datos.append(nuevoDato)
print("Los datos al reves son: ")
for i in range(6,0,-1):
    print(datos[i-1])
