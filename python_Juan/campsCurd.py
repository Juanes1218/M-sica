import json

with open('campers_inscritos.json', 'r', encoding="utf8") as file:
    mijson = json.load(file)

    def mainCamper():
        estado = "Inscrito"
        nuevo_id = max([inscripcion["id"] for inscripcion in mijson['datos']['inscripciones']], default=0) + 1
        
        nueva_inscripcion = {}
        nueva_inscripcion['id'] = nuevo_id
        nueva_inscripcion['Identificacion'] = int(input("Numero de identificacion "))
        nueva_inscripcion['Nombre'] = input("Nombre: ")
        nueva_inscripcion['Apellido1'] = input("Primer apellido: ")
        nueva_inscripcion['Apellido2'] = input("Segundo apellido: ")
        nueva_inscripcion['Direccion'] = input("Dirección: ")
        nueva_inscripcion['Acudiente'] = input("Acudiente (si no tiene, dejar en blanco): ")
        nueva_inscripcion['Celular'] = int(input("Numero de celular: "))
        nueva_inscripcion['Telefono'] = int(input("Numero de telefono: "))
        nueva_inscripcion['Estado'] = estado

        mijson['datos']['inscripciones'].append(nueva_inscripcion)
        
        with open('inscritos.json', 'w', encoding="utf8") as file:
            json.dump(mijson, file, indent=2)
    
    mainCamper()