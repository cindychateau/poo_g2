from Persona import Persona
from Estudiante import Estudiante
from Maestro import Maestro

elena = Persona("Elena", "De Troya", 30) #Instancia de Persona

juana = Persona("Juana", "De Arco", 33)

pablo = Persona("Pablo", "Picasso", 55)

pedro = Estudiante("Pedro", "Infante", 42, 1, "Web Fundamentals")

cynthia = Maestro("Cynthia", "Castillo", 30, "Python")

print(elena.nombre)
print(juana.nombre)

juana.cumpleanios()
print(juana.edad)

elena.codificar(101)
print(elena.lineas_codigo)

elena.codificar(40)
juana.codificar(20)
print(elena.lineas_codigo)
print(juana.lineas_codigo)
print(Persona.total_lineas_codigo)

Persona.cambiar_pais("México")

if Persona.mayoria_edad(19):
    print("Wow, si eres mayor de edad")

juana.nombre = "Juanita"

#pedro.imprimir()

Persona.imprime_lista()

pedro.que_haces()
cynthia.que_haces()

Estudiante.imprime_lista()