import usuarios.usuarios as u
import getpass #Para leer entradas sin mostrar los caracteres
import notas.acciones as note
class Acciones:
    def registro(self):
        print("Ok! Registrar")
        nombre = input("Ingresar nombre: ")
        apellidos = input("Ingresar apellidos: ")
        email = input("Ingresar email: ")
        password = getpass.getpass("Ingresa constraseña: ")
        usuario = u.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()
        if registro[0]>=1:
            print(f"El usuario {registro[1].email} ha sido registrado")
        else: 
            print("El registro falló")
        print("*"*100)

    def login(self):
        print("Ok! Autenticar")
        email = input("Ingresar email: ")
        password = getpass.getpass("Ingresa la contraseña: ")
        usuarioLogeado = u.Usuario('','',email,password)
        login= usuarioLogeado.identificar()
        if login is not None:
            print(f"Bienvenido {login[1]}")
            self.proximasAcciones(login)
        else:
            print("Usuario o contraseña no son correctos")
        print("*"*100)

    def proximasAcciones(self,usuario):
        print(""" Opcion a realizar:
                - Crear nota (1)
                - Mostrar nota (2)
                - Eliminar nota (3)
                - Editar nota (4)
                - Salir (5)
            """)
        accion = input("Inserta la opción deseada: ")
        while accion != "1" and accion != "2" and accion!= "3" and accion != "4" and accion!="5":
            print("Esa no es una opción correcta, escriba de nuevo")
            accion = input("Inserta la opción deseada: ")
        
        notaHazEl = note.Acciones()

        if accion=="1":
            print("Crear nota")
            notaHazEl.crear(usuario)
            print("*"*100)
            self.proximasAcciones(usuario)

        elif accion =="2":
            print("Mostrar nota")
            notaHazEl.listar(usuario)
            print("*"*100)
            self.proximasAcciones(usuario)

        elif accion =="3":
            print("Eliminar nota")
            notaHazEl.borrado(usuario)
            print("*"*100)
            self.proximasAcciones(usuario)

        elif accion =="4":
            print("Editar nota")
            print("""
                    Desea editar:
                    - Titulo (1)
                    - Descripcion (2)
                  """)
            edit= input("Escriba la opción: ")
            while edit !="1" and edit !="2":
                edit = input("Escriba una opción correcta: ")
            
            if edit == "1":
                notaHazEl.edita_titulo(usuario)
            else:
                notaHazEl.edita_descripcion(usuario)
            print("*"*100)
            self.proximasAcciones(usuario)
        else:
            print("Saliendo")
            print("*"*100)
            exit()


