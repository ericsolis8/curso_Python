import random
import time
def mostrarIntro(): # def crea una funcion
   print('Estás en una tierra llena de dragones. Frente a tí')
   print('hay dos cuevas. En una de ellas, el dragón es generoso y')
   print('amigable y compartirá su tesoro contigo. El otro dragón')
   print('es codicioso y está hambriento, y te devorará inmediatamente.')
   print()
def elegirCueva(): #funcion pregunta que cueva elige
    cueva = '' #declara variable guardara la eleccion
    while cueva != '1' and cueva != '2': #true and true
        print("¿Elige una cueva? (1 ó 2)")
        cueva = input()
    return cueva
def explorarCueva(cuevaElegida): #mostrando resultados del juego
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡El dragon aparece súbitamente frente a tí! Abre sus fauces y...')
    print()
    time.sleep(2)
    cuevaAmigable = random.randint(1,2) #aleatoriamente selecciona una de las dos opciones
    if cuevaElegida == str(cuevaAmigable): #compara la eleccion con la cueva amigable
        print("¡Te regala un tesoro!")
    else:
        print("¡Te avienta fuego por la boca!")
jugarDeNuevo = "si"
while jugarDeNuevo == "si" or jugarDeNuevo == "s": #pregunta si deseas volver a correr el código
    mostrarIntro()
    numeroDeCueva = elegirCueva()
    explorarCueva(numeroDeCueva)
    print("¿Quieres jugar de nuevo? (si ó no)")
    jugarDeNuevo = input()