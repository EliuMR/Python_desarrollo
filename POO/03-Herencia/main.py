import clases

persona =clases.Persona()
persona.setNombre("Julio")
persona.setApellidos("Robles")
persona.setAltura("167 cm")
persona.setEdad(57)

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("-"*50)
informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Duran")
print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Los lenguajes que conoce son: {informatico.getLenguajes()}")

print("-"*50)
tecnico=clases.TecnicoRedes("Experto",4)
tecnico.setNombre("Manolo") 
tecnico.setApellidos("Nuñez")
print(f"El tecnico es {tecnico.getNombre()} {tecnico.getApellidos()}")
print(f"Sabe: {tecnico.getLenguajes()}")
print(f"Es {tecnico.getAuditarRedes()} con {tecnico.getExperienciaRedes()} años en redes")

