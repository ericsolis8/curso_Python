a=34
b=33
c=200
'''
if b > a:
    print("b es mayor que a")
elif a == b:
    print("ambas son iguales")
else:
    print("a es mayor que b")
'''
'''
#una linea si la declaracion
if a > b: print("a es mayor que b")
#una linea si otra declaracion
print("A") if a > b else print("B")
#una linea si otra declaracion, con 3 condiciones
print("A") if a > b else print("=") if a == b else print("B")
'''
if a > b and c > a:
    print("Ambas condiciones son verdaderas")


