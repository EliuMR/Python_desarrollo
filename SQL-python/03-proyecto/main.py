from usuarios import acciones
def main():
    print("*"*100)
    print("""
        Acciones disponibles:
            - Registrar
            - Autenticar
        """)

    accion = input("Accion: ")
    print("*"*100)
    hazEl =acciones.Acciones() # 

    while accion != "Registrar" and accion != "registrar" and accion != "Autenticar" and accion != "autenticar":
        print("Accion no disponible. Escriba una opción válida.")
        accion = input("Accion: ")

    if accion == "Registrar"  or accion == "registrar":
        hazEl.registro()

    elif accion == "Autenticar" or accion == "autenticar":
        hazEl.login()

if __name__ == "__main__":
    main()
