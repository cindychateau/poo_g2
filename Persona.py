class Persona:

    pais = "Colombia"
    total_lineas_codigo = 0

    #A traves de init INICIALIZAMOS nuestra instancia.
    def __init__(self, nombre, apellido, edad): #SELF nos incluye toda la información correspondiente al objeto individual o instancia
        #nombre = "Elena", apellido = "De Troya", edad = 30
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.lineas_codigo = 0
    
    def cumpleanios(self):
        self.edad += 1
        if Persona.mayoria_edad(self.edad): #True
            print("Wuju, eres mayor de edad!")

    def tomar_cerveza(self):
        if Persona.mayoria_edad(self.edad): 
            print("Aquí está tu cerveza")
        else:
            print("Lo siento, no puedes tomar")
    

    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo += cantidad_lineas

    @classmethod
    def cambiar_pais(cls, nuevo_pais): 
        #nuevo_pais = "Mexico"
        cls.pais = nuevo_pais

    @staticmethod
    def mayoria_edad(edad):
        if edad > 18:
            return True
        else:
            return False