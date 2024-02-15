import os
from colorama import Fore
import campus
import json


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
            print(campus.mainCamper)


            input("Presiona Enter para continuar...")

        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción válida.")


def NotasFundamentosProgramacion():
 
    with open('Notas.json', 'r', encoding="utf8") as file:
        notas_data = json.load(file)
    
    with open('Salones.json', 'r', encoding="utf8") as file:
        salones_data = json.load(file)

    alumnos_notas = notas_data['Notas']['Matriculados']

    telefono = int(input("Digite el Telefono: "))

    for alumno_notas in alumnos_notas:
        if alumno_notas['Telefono'] == telefono:
            nota_prueba_teorica = float(input("Digite nota de la prueba teórica (0 a 100): ")) * 0.3
            nota_prueba_practica = float(input("Digite nota de la prueba práctica (0 a 100): ")) * 0.6
            
            print("Digite la cantidad de quizes realizados durante el módulo: ")
            cantidad_quizes = int(input("--->"))
            suma_quizes = 0
            for j in range(cantidad_quizes):
                nota_quiz = int(input(f"Digite nota del quiz #{j + 1} (0 a 100): "))
                suma_quizes += nota_quiz
            promedio_quizes = suma_quizes / cantidad_quizes

            print("Digite la cantidad de trabajos realizados durante el módulo: ")
            cantidad_trabajos = int(input("--->"))
            suma_trabajos = 0
            for k in range(cantidad_trabajos):
                nota_trabajo = int(input(f"Digite nota del trabajo #{k + 1} (0 a 100): "))
                suma_trabajos += nota_trabajo
            promedio_trabajos = suma_trabajos / cantidad_trabajos
            
            total_talleres = (promedio_quizes + promedio_trabajos) / 2 * 0.1
            nota_final = nota_prueba_practica + nota_prueba_teorica + total_talleres
            
            rendimiento = "Riesgo Bajo" if nota_final >= 60 else "Bajo rendimiento"

            for salon_numero, salon_info in salones_data['Salones'].items():
                for alumno_salon in salon_info['Alumnos']:
                    if alumno_salon['Telefono'] == telefono:
                        alumno_salon['Nota_final_Fundamentos'] = nota_final
                        alumno_salon['Rendimiento_Fundamentos'] = rendimiento
                        break
            
            break 
        
    with open('Salones.json', 'w', encoding="utf8") as file:
        json.dump(salones_data, file, indent=2)
