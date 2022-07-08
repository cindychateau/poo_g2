from Persona import Persona

class Maestro(Persona):

    def __init__(self, nombre, apellido, edad, curso):
        super().__init__(nombre, apellido, edad)
        self.curso = curso

    def que_haces(self):
        print("Estoy enseñando a mis alumnos a programar")