from  funciones import limpiar_pantalla, mostrar_menu_principal, menu_campers, menu_coordinador

while True:
        limpiar_pantalla()
        mostrar_menu_principal()
        rol = input("---->")
        if rol == '1':
            menu_coordinador()
        elif rol == '2':
            print("Funcionalidad de Trainer aún no implementada")
            input("Presiona Enter para continuar...")
        else:
            print("Rol no válido. Por favor, elige una opción válida.")

        salir = input("¿Deseas salir? (s/n): ")
        if salir.lower() == 's':
            print("¡Hasta luego!")
            break