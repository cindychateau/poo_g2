from Persona import Persona

elena = Persona("Elena", "De Troya", 30) #Instancia de Persona

juana = Persona("Juana", "De Arco", 33)

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