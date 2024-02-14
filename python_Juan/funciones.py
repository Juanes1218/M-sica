import os
from colorama import Fore
import campsCurd



def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')

def mostrar_menu_principal():
    print(Fore.BLUE + "--------------------------------")
    print("--                            --")
    print("--         BIENVENIDO         --")
    print("--                            --")
    print("--------------------------------")
    print("")
    print("Escoge tu rol")
    print("")
    print("1 Coordinador\t2 Trainer")
    print("")

def menu_coordinador():
    while True:
        limpiar_pantalla()
        print(Fore.MAGENTA + "--------------------------------")
        print("--                            --")
        print("--   BIENVENIDO COORDINADOR   --")
        print("--                            --")
        print("--------------------------------")
        print("")
        print("¿Dónde deseas ingresar?")
        print("") 
        print("1 CAMPERS\t 2 Trainers")
        a = input("---->")
        print("")
        if a == '1':
            menu_campers()
        elif a == '2':
            print("Funcionalidad de Trainer aún no implementada")
        else:
            print("Rol no válido. Por favor, elige una opción válida.")

def menu_campers():
    while True:
        limpiar_pantalla()
        print("-----------------")
        print("--             --")
        print("--   CAMPERS   --")
        print("--             --")
        print("-----------------")
        print("")
        print("1. Rendimiento de los campers\n2. Matricular campers \n3. Inscribir campers\n4. Volver ")
        opcion = input("---->")
        if opcion == '1':
            limpiar_pantalla()
            print("---------------------------------")
            print("--                             --")
            print("--     RENDIMIENTO CAMPERS     --")
            print("--                             --")
            print("---------------------------------")
            input("Presiona Enter para continuar...")
        elif opcion == '2':
            limpiar_pantalla()
            print("---------------------------------")
            print("--                             --")
            print("--     MATRICULAR CAMPERS      --")
            print("--                             --")
            print("---------------------------------")
            input("Presiona Enter para continuar...")
        elif opcion == '3':
            limpiar_pantalla()
            print("---------------------------------")
            print("--                             --")
            print("--     INSCRIBIR CAMPERS       --")
            print("--                             --")
            print("---------------------------------")
            print(campsCurd.mainCamper)


            input("Presiona Enter para continuar...")

        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción válida.")