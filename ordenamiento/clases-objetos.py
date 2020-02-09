'''
class persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = persona("Jhon", 22)

print(p1.name)
print(p1.age)
'''
'''
class persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def funcion(self):
        print("Hola mi nombre es: ",self.name)

p1 = persona("Jhon", 22)
p1.funcion()
'''
class Persona:
    def __init__(self, nombre, apellido):
        #propiedades del objeto
        self.firstname = nombre
        self.lastname = apellido
    #método de la clase
    def printname(self):
        print(self.firstname, self.lastname)

#usa la clase persona para crear un objeto, y luego ejecuta el metodo imprime nombre
x = Persona("Jhon", "Doe")
x.printname()
