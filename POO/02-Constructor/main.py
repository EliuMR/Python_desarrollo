#importamos la clase
from coche import Coche


carro01 = Coche("morado","reanult","clio",120,230,1)
carro02 = Coche("azul","bmw","q5",150,600,6)
carro03 = Coche("amarillo","vw","platina",70,200,4)
carro04 = Coche("rojo","audi","a1",180,700,2)


print(carro01.getInfo())#Definir una clase 
print(carro02.getInfo())#Definir una clase 
print(carro03.getInfo())#Definir una clase 
print(carro04.getInfo())#Definir una clase 

#Detectat tipado
if type(carro01) == Coche:
    print("Es un objeto de la clase")
else:
    print("No es un objeto")

#Visibilidad
#Estamos obteniendo el atributo privado, esto porque existe una función para obtener dicho atributo, si no, no se podría obtener de otra forma
print(carro01.getPrecio())
