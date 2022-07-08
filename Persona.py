class Persona:

    pais = "Colombia"
    total_lineas_codigo = 0
    lista = [] #lista = [elena, juana]

    #A traves de init INICIALIZAMOS nuestra instancia.
    def __init__(self, nombre, apellido, edad): #SELF nos incluye toda la información correspondiente al objeto individual o instancia
        #self = juana, nombre = "Juana", apellido = "De Arco", edad = 33
        self.nombre = nombre #juana.nombre = "Juana"
        self.apellido = apellido #uana.apellido = "De Arco"
        self.edad = edad #juana.edad = 33
        self.lineas_codigo = 0 #juana.lineas_codigo = 0
        Persona.lista.append(self) #Agrégale a juana
    
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

    def imprimir(self): #SELF implícito-> self = elena 
        print("Nombre:"+self.nombre+" Apellido:"+self.apellido+" Edad:"+str(self.edad))

    def que_haces(self):
        raise NotImplementedError

    @classmethod
    def cambiar_pais(cls, nuevo_pais): 
        #nuevo_pais = "Mexico"
        cls.pais = nuevo_pais

    #lista = [elena, juana]
    #persona = elena
    #FUNCION IMPRIMIR para ELENA
    #persona = juana
    #FUNCION IMPRIMIR para JUANA
    @classmethod
    def imprime_lista(cls): #Persona
        for persona in cls.lista:
            persona.imprimir()

    @staticmethod
    def mayoria_edad(edad):
        if edad > 18:
            return True
        else:
            return False