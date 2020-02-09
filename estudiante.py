class Estudiante(objeto):
    def __init__(self, nombre):
        self.nombre = nombre
    def establece_edad(self, edad):
        self.edad = edad
    def establece_licenciatura(self, licenciatura):
        self.licenciatura = licenciatura
anna = Estudiante('Anna')
anna.establece_edad(21)
anna.establece_licenciatura('Sistemas')