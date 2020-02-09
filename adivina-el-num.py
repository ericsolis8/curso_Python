import random
intentos = 0 #declara una variable intentos.
print("Hola, como te llamas?")
nombre=input() #obtiene nombre y lo almacena en una variable nombre.
numero = random.randint(1,10) #devuelve un entero aleatorio en el intervalo comprendido.
print("Bueno "+nombre+", estoy pensando en un numero entre 1 y 10.")
while intentos < 3: #sentencia solo 3 intentos
    print("Escribe cual crees que es?")
    estimacion = input() #primer intento
    estimacion = int(estimacion) #devuelve un entero de un argumento.
    intentos = intentos + 1 #contador intentos
    if estimacion < numero:
        print("Tu estimacion esta por debajo.")
    if estimacion > numero:
        print("Tu estimacion es muy alta.")
    if estimacion == numero:
        break #sentencia / abandona el bucle anticipadamente.
if estimacion == numero:
    intentos = str(intentos)
    print("Bien "+nombre+ "! Haz adivinado el número en "+intentos+ " intentos")
if estimacion != numero:
    numero = str(numero)
    print("Game Over.\nEl numero era: "+numero)
