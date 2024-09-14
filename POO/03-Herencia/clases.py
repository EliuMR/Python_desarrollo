#Herencia es la capacidad de compartir atributos y que diferentes clases hereden de otras

class Persona():

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad()

    def setNombre(self,nombre):
        self.nombre=nombre

    def setApellidos(self,apellidos):
        self.apellidos=apellidos

    def setAltura(self,altura):
        self.altura=altura
    
    def setEdad(self,edad):
        self.edad=edad


    def hablar(self):
        return "Ich bin Männ"

    def bebe(self):
        return "Ich trinke Wasser"

    def comer(self):
        return "Ich essen ein Apfel"


class Informatico(Persona):
    def __init__(self):
        self.lenguajes="HTML,CSS,JS,PHP"
        self.experiencia=4

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguaje):
        self.lenguajes += lenguaje
        return self.lenguajes

    def programas(self):
        return "Print"

class TecnicoRedes(Informatico):
        def __init__(self,auditarRedes,experienciaRedes):
            super().__init__() #Llamar el constructor de la clase padre, por defecto no lo inicializa
            self.auditarRedes = auditarRedes
            self.experienciaRedes = experienciaRedes

        def getExperienciaRedes(self):
            return self.experienciaRedes

        def getAuditarRedes(self):
            return self.auditarRedes
