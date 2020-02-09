salir=0
resultado=0
while salir==0:
    num1=input("Escribe un numero: ")
    num2=input("Escribe un segundo numero: ")
    calcular=input("Escribe que operacion deseas realizar: ")
    if calcular == "suma":
        suma = num1 + num2
        print (suma)
terminar = input("Salir S/N")
if terminar == "s":
    salir=1
else:
    salir=0
    
