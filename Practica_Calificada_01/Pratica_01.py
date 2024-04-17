empleados=[]

salarios_por_trabajo = {
    "Limpieza": 1025,
    "Mesero": 1500,
    "Cajero": 1500,
    "Vigilante": 1400,
    "Gerente": 2500
}

    

def ingresar_empleado():
    id_empleado =input("ingrese el id del empleado: ")
    nombre=input("Ingrese el nombre del empleado: ")
    dni=input("Ingrese el dni del empleado: ")
    telefono=input("Ingrtese el telefono del empleado: ")
    tiempo=input("ingrese el teiempo del empleado (meses): ")
    print ("Ingrese el trabajo que realizara: ")
    print("Limpieza")
    print("Mesero")
    print("Cajero")
    print("Vigilante")
    print("Gerente")
    opcion_trabajo= input("Seleccione una opcion:")

    if opcion_trabajo in salarios_por_trabajo:
        salario= salarios_por_trabajo[opcion_trabajo]
        empleado = {"id": id_empleado, "nombre": nombre, "dni": dni, "telefono": telefono, "tiempo": tiempo, "trabajo": opcion_trabajo, "salario": salario}
        empleados.append(empleado)
        print("El empleado a sido ingresado con exito")

    
    


def main():
    
    while True:
        print ("bienvenidos")
        print ("1. Ingresasr nuevo empleado")
        print ("2. Mostrar lista de empleados")
        print ("3. salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            ingresar_empleado()
        elif opcion == "2":
            if not empleados:
                print("no hay empleados aun")
            else:
                print("lista de empleados")
                for empleado in empleados:
                    print(f"id:{empleado['id']},Nombre: {empleado['nombre']},DNI: {empleado['dni']},Telefono: {empleado['telefono']},tiempo: {empleado['tiempo']},trabajo: {empleado['trabajo']}, salario: {empleado['salario']}")
                print()
        elif opcion == "3":
            print("Adios")
            break
        else:
            print("Ingrese una opcion valida")

if __name__ == "__main__":
    main()


