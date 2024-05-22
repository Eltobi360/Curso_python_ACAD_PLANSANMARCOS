from datetime import date
trabajadores = []

class Trabajador:
    def __init__(self,nombre, apellido,DNI,Tiempo_lb):
        self.nombre=nombre
        self.apellido= apellido
        self.dni=DNI
        self.tiempo_trabajando=Tiempo_lb
    
    def mostrar_Info(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}")
        print(f"DNI : {self.dni}")
        print(f"Tiempo en la empresa: {self.tiempo_trabajando}")


class Desarollador(Trabajador):
    
    salario_base=3500
    porcentaje_aumento=0.05
    def __init__(self, nombre, apellido, DNI, Tiempo_lb,lenguaje):
        super().__init__(nombre, apellido, DNI, Tiempo_lb)
        self.lenguaje_de_programacion=lenguaje
        
        self.salario = CalculadorContable.calcular_salario(
            Desarollador.salario_base, Tiempo_lb, Desarollador.porcentaje_aumento)
  
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje de Programación: {self.lenguaje_de_programacion}")
        print(f"Salario: {self.salario:.2f}")
   
   
        
class Diseñador(Trabajador):

    salario_base=2200
    procentaje_aumento=0.003
    def __init__(self,nombre, apellido, DNI, Tiempo_lb,programa_de_diseño ):
        super().__init__(nombre, apellido, DNI, Tiempo_lb)
        self.programa=programa_de_diseño
        self.salario=""

class CalcularSalarios:
    @staticmethod
    def calular_salarioTotal(Trabajador):
        
        return 

class CalculadorContable:
    pass



Trabjador_1 = Trabajador("Mauricio","Neyra",123421,4)
print (Trabjador_1.nombre)
print(Trabjador_1.apellido)
print (Trabjador_1.dni)
print (Trabjador_1.tiempo_trabajando)