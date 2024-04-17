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
    print("1.Limpieza")
    print("2.Mesero")
    print("3.Cajero")
    print("4.Vigilante")
    print("5.Gerente")
    opcion_trabajo= input("Seleccione una opcion -> 'Mesero': ")

    if opcion_trabajo in salarios_por_trabajo:
        salario= salarios_por_trabajo[opcion_trabajo]
        empleado = {"id": id_empleado, "nombre": nombre, "dni": dni, "telefono": telefono, "tiempo": tiempo, "trabajo": opcion_trabajo, "salario": salario}
        empleados.append(empleado)
        print("El empleado a sido ingresado con exito")
    else:
        print("Ingrese una opcion valida")
    
    

def buscar_empleado():
    id_buscar= input("Ingrese el id del empleado: ")
    empleados_encontrado=None

    for empleado in empleados: 
        if empleado["id"]== id_buscar:
            empleados_encontrado=empleado
            break

    if empleados_encontrado:
        print("El empleado encontrado: ")
        print(f"id:{empleado['id']},Nombre: {empleado['nombre']},DNI: {empleado['dni']},Telefono: {empleado['telefono']},tiempo: {empleado['tiempo']},trabajo: {empleado['trabajo']}, salario: {empleado['salario']}")
    else:
        print("No se encontro")




def main():
    
    while True:
        print ("=================================")
        print ("bienvenidos")
        print ("=================================")
        print ("1. Ingresasr nuevo empleado")
        print ("2. Mostrar lista de empleados")
        print ("3. Visualizar informacion de un empleado")
        print ("=================================")
        print ("4. salir")

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
            buscar_empleado()
        elif opcion == "4":
            print("Adios")
            break
        else:
            print("Ingrese una opcion valida")

if __name__ == "__main__":
    main()


