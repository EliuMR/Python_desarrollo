import notas.nota as notas
class Acciones:
    def crear(self,usuario):
        print("Ok, crear nota")
        titulo = input ("Titulo de nota: ")
        descripcion = input("Nota: ")
        nota = notas.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        if guardar[0] >=1:
            print("Nota agregada")
        else:
            print("Error, nota no se ha guardado") 

    def listar(self,usuario):
        print("Ok, listar notas")
        nota = notas.Nota(usuario[0],'','')
        lista,bandera = nota.mostrar()
        if bandera==True:
            for i in lista:
                print(i)
        else:
            print (f"El usuario: {usuario[3]} no tiene notas para mostrar")

    def borrado(self,usuario):
        print("Ok, borrar nota")
        id_nota = input("Inserta el id de la nota a modificar: ")
        nota = notas.Nota(usuario[0],'','')
        borra = nota.borrar(id_nota)
        if borra >0:
            print(f"Se ha borrado la nota con id:{id_nota}")
        elif borra==0:
            print("Esa nota no te pertenece o no existe")


    def edita_titulo(self,usuario):
        print("Ok, editar titulo")
        id_nota = input("Inserta el id de la nota a modificar: ")
        titulo_nuevo = input("Inserta el nuevo titulo: ")
        nota = notas.Nota(usuario[0],"","")
        edita = nota.editar_titulo(id_nota,titulo_nuevo)
        if edita >0:
            print(f"Se ha modificado el titulo de la nota: {id_nota}")
        else:
            print(f"Esa nota no se puede modificar ya que no existe o no te pertenece")

    def edita_descripcion(self,usuario):
        print("Ok, editar descripcion")
        id_nota = input("Inserta el id de la nota a modificar: ")
        descripcion_nueva = input("Inserta la nueva descripción: ")
        nota = notas.Nota(usuario[0],"","")
        edita = nota.editar_descripcion(id_nota,descripcion_nueva)
        if edita >0:
            print(f"Se ha modificado la descripción de la nota: {id_nota}")
        else:
            print(f"Esa nota no se puede modificar ya que no existe o no te pertenece")
