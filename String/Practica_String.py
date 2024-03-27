Correro="mneyraarzapalo@gmail.com"
print(type(Correro))

mensaje="Tu correro es "+ Correro
print(mensaje)

print("Mauricio\nJorge\nNeyra\nArzpalo")

print(r"Mauricio\nJorge\nNeyra\nArzpalo")

letra_de_cancion="""\
line1
line2
line3

parafo1

line1
line2
line3

parafo2\
"""
"""
Este es un comentario de multiples lineas 
tambien nos ayuda a guardar string sin neceidad de agregar saltos de lineas 
"""


print(letra_de_cancion)


menu="""\
Ingrese una opcion de calculo

1.Suma de dos numeros
2.resta de dos numeros
3.calcular interes

\
"""


print(menu)


nombre_completo= "'Jorge' ,'Mauricio', 'Neyra'"

print(nombre_completo)


presentacion ="Mi nombre es: " + nombre_completo
print(presentacion) 


coutry ="Peru"

pais="Republica Dominicana"


print(pais[2])
print(pais[-4])

print("El indice del pasi en la posion 2 es : ", pais[2])
print("El indice del pais en la posion -4 es :", pais[-4])


print(len(pais))

print(pais[0:9])

print(pais[:9])


print(pais[10:])

print(pais[:-3])


#Formula

print(pais[:9] + pais[9:])