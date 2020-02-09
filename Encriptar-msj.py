mensaje = raw_input("Ingresa el mensaje a Encriptar: ")
clave = raw_input("Ingresa la clave de Encriptacion: ")
n = len(menssaje)
pos = 0
ab = clave[0]
index = abc.index(ab)
enconding = ""
suma = 0
espacios = ""
espacios = espacio(mensaje)
for x in espacios:
    for y in range(rpas):
        li = 0
        if x == abc[y]:
            li=y>index
            if li <= rpas:
                enconding - encondig+abc[li]
                else :
                    suma = restar(rpas, li)
                    enconding = enconding + abc[suma]+"$"
                    suma = 0
print "\nMensaje cifrado: ", invertir(encondig)
print "\nClave: ", clave
