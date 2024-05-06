import aplicacion

def mostrar_menu():
    print("_____________MENU___________\n"+
          "1. Crear archivo\n"+
          "2. Eliminar archivo\n"+
          "3. Agregar contenido\n"+
          "4. Mostrar contenido de archivo\n"+
          "5. Salir"
          )             
    while True:
        opcion = input("Elija una opción (1-5): ")
        if opcion == "1":
            aplicacion.crear_archivo()
        elif opcion == "2":
            aplicacion.eliminar_archivo()
        elif opcion == "3":
            aplicacion.agregar_contenido()
        elif opcion == "4":
            aplicacion.mostrar_contenido()
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida (1-5).")

mostrar_menu()
