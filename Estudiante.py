from Persona import Persona

class Estudiante(Persona):

    lista_estudiantes = []

    def __init__(self, nombre, apellido, edad, id, curso):
        super().__init__(nombre, apellido, edad)
        self.id = id
        self.curso = curso
        Estudiante.lista_estudiantes.append(self)

    #ANULACION
    def imprimir(self):
        #print("Nombre:"+self.nombre+" Apellido:"+self.apellido+" Edad:"+str(self.edad)+" Curso:"+self.curso)
        super().imprimir()
        print("Curso:"+self.curso)

    def estudiar(self):
        print("Estamos leyendo un nuevo tema")

    def que_haces(self):
        print("Estoy estudiando en Coding Dojo y aprendiendo muchísimo!")

    @classmethod
    def imprime_lista(cls): #Persona
        for persona in cls.lista_estudiantes:
            persona.imprimir()