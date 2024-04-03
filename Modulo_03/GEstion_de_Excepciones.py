x=10
y=0

"""try: 
    resultado = x/y
except zerodivisionerror as error:
    print ("Lo sentimos, se necontro el siguiente error \n", error)
"""

a="hola"
b=20

"""try: 
    concatenar = a+b
except (ZeroDivisionError):
    print("Lo sentimos, ocurrio un error")
"""
"""
==================================================
try:
    numero1= int(input("ingrese un numero1 -> "))
    numero2= int(input("ingrese un numero2 -> "))              
    resultado_suma= numero1+numero2
    resultado_division= numero1 / numero2
    print(resultado_suma)
    print(resultado_division)
except (ZeroDivisionError, ValueError):
    print("Ingreso un numero valido")
except KeyboardInterrupt:
    print("Se detuvo el programa")
=================================================
"""

# Crear nuestras propias exepciones 
    
try: 
    a = int(input("Ingrese un valor para el numero a ->"))
    b = int(input("Ingrese un valor para el numero b ->"))
    if b==0:
        raise ZeroDivisionError ("b no puede tomar el valor de 0",a , b)
except ZeroDivisionError as error:
    print(error)
    print(error.args[0])
    print(error.args[1])
    print(error.args[2])