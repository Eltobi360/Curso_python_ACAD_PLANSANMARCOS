suma = lambda num1,num2: num1 + num2
print (suma(10,20))

potencia = lambda num1,num2: num1 + num2
print (potencia(10,230))

def crear_lista_impares(limite_lista, func):
    aux = [element for element in range(limite_lista)if func(element)]
    return aux

lista_impares = crear_lista_impares(20,lambda n: True if n % 2 !=0 else False)
print (lista_impares)