#Programación POO

#Definir una clase 
class Coche:
    #Atributos
    color = "rojo"
    marca = "BMW"
    modelo = "1"
    velocidad = 300
    caballaje = 500
    concesionarios =2
    
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

#Crear objeto / Instaciar la clase
coche = Coche() #creamos el objetos
print(coche) #Accedemos a uno de sus atributos
print("Marca: ",coche.marca)
print("Velocidad: ",coche.getVelocidad()) #La manera más recomendable de acceder a los atributos del objeto es con funciones geter
print("Vamos a acelerar: ")
for i in range(5):
    coche.acelerar()
    print("Velocidad: ",coche.getVelocidad())
coche.setColor("Amarillo")
print(coche.getColor()) # De igual manera la manera más recomendable de cambiar atributos es con metodos seter

print("-"*20)

print("Coche 2")
#Creando varios objetos
coche2 = Coche()
coche2.setColor("verde")
coche2.setModelo("Gallardo")
print(coche2.marca,coche2.getColor(),coche2.getModelo())


