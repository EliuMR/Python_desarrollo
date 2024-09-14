#Definir una clase 
class Coche:
    #Atributos
    color = "rojo"
    marca = "BMW"
    modelo = "1"
    velocidad = 300
    caballaje = 500
    concesionarios =2
    
    #Atributos privados, con __
    __precio = 350000

    #constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,concesionarios):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.concesionarios = concesionarios

    #Métodos, acciones que realiza el objeto (cambiar valores, obtener atributos)
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -=1
    def getVelocidad(self):
        return self.velocidad
    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo  = modelo
    def getModelo(self):
        return self.modelo
    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca

    def getInfo(self):
        info = "Información del coche:"
        info += "\n Color: "+ self.getColor()
        info += "\n Marca: "+ self.getModelo()
        info += "\n Modelo: " +self.getMarca()
        info += "\n Velocidad: "+str(self.getVelocidad())

        return info

    #Función para obtener el atributo privado, se recomienda que todos los atributos sea 
    #privados y que se modifiquen o lean con funciones setter o getter
    def getPrecio(self):
        return self.__precio
