#-*- coding: utf-8-*-
print("CALCULADORA CON PYTHON")
print("")
print("1)SUMAR,2)RESTAR,3)MULTIPLICAR,4)DIVIDIR")
opcion=(input("Elija una opción: "))
primer_num=input("Ingresa un número: ")
segundo_num=input("Ingresa un segundo número: ")
if opcion == 1:
    suma = (primer_num + segundo_num)
    print(suma)
elif opcion == 2:
    resta = primer_num - segundo_num
    print("La resta de los números es: ",resta)
elif opcion == 3:
    multi = primer_num * segundo_num
    print("La multiplicación de los numeros es: ",multi)
elif opcion == 4:
    division = primer_num / segundo_num
    print("La division de los numeros es: ",division)
else:
    print("opcion fallida")
