import pylab as pl
import numpy as np

# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada
pl.figure(figsize=(10, 6), dpi=80)
 #pl.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
 #pl.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
 #pl.legend(loc='upper left')

# Crear una nueva subgráfica en una rejilla de 1x1
pl.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Graficar la función coseno con una línea continua azul de 1 pixel de grosor
pl.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Graficar la función coseno con una línea continua verde de 1 pixel de grosor
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Establecer límites del eje x
pl.xlim(-4.0, 4.0)


# Ticks en x
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Establecer límites del eje y
pl.ylim(-1.0, 1.0)

# Ticks en y
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Guardar la figura usando 72 puntos por pulgada
# savefig("exercice_2.png", dpi=72)

# Mostrar resultado en pantalla
pl.show()