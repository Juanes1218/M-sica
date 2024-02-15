import json

def MainCamperAñadir():
    with open('campers_inscritos.json', 'r', encoding="utf8") as file:
        mijson = json.load(file)
    
    def mainCamper():
        estado = "Inscrito"
        nuevo_id = max([inscripcion["id"] for inscripcion in mijson['datos']['inscripciones']], default=0) + 1
        
        nueva_inscripcion = {}
        nueva_inscripcion['id'] = nuevo_id
        nueva_inscripcion['Identificacion'] = int(input("Escriba el número de identificación: "))
        nueva_inscripcion['Nombre'] = input("Escriba el nombre: ")
        nueva_inscripcion['Apellido1'] = input("Escriba el apellido 1: ")
        nueva_inscripcion['Apellido2'] = input("Escriba el apellido 2: ")
        nueva_inscripcion['Direccion'] = input("Escriba la dirección: ")
        nueva_inscripcion['Acudiente'] = input("Escriba el nombre de su acudiente (opcional): ")
        nueva_inscripcion['Celular'] = int(input("Escriba el número de celular: "))
        nueva_inscripcion['Telefono'] = int(input("Escriba el número de teléfono: "))
        nueva_inscripcion['Estado'] = estado

        mijson['datos']['inscripciones'].append(nueva_inscripcion)
        
        with open('inscritos.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=2)
    
    mainCamper()