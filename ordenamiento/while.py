'''
#imprime i mientras sea menor que 6
i=1
while i < 6:
    print(i)
    i+=1
'''
'''
#salir del bucle cuando sea 3
i=1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1
'''
'''
#continua si la siguiente es 3
i=0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
'''
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("(i) ya no es menor que 6")
