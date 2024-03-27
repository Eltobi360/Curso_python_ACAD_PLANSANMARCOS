nombre_alumno="Mauricio"
titulo_libro="la sociedad de la nieve"

#capitaliza()

print(titulo_libro.capitalize())

titulo_correcto = titulo_libro.capitalize()

print("Metodo capitalize: ", titulo_correcto)


print("Metodo upper: ", nombre_alumno.upper())


print("HOLA ME LLAMO MAURICIO".lower())

print("METODO title:", titulo_libro.title())


mensaje="       me olvide que decir             "

print("Totla de caracteres de mensaje: ",len(mensaje))

nuevo_mensaje= mensaje.strip()
print("Total de caracteres de mensaje tras eliminar espacios en blanco: ", len(nuevo_mensaje))
print(nuevo_mensaje)

#Adicional : esta funcion tambien acepta un argumento / parametro

print("abc  asdddddddfasfdasfasfa abc".strip("abc"))



#6. rstrip() -> right strip, derecha
# Lstrip() -> left strip, izquierdo

mensaje_bizarro="abc asdasdasdasdasfdsfaw               "
print(len(mensaje_bizarro))
nuevo_mensaje=mensaje_bizarro.rstrip()
print(len(nuevo_mensaje))


print("abc asdasdasdasdasfdsfaw               ".rstrip("abc"))
print("abc asdasdasdasdasfdsfaw               ".lstrip("abc"))


#metodo isdigit() -> retorna true si los caracteres son digitos del 0 al 9
#metodo isnumeric()
is_digit="1234".isdigit()
print("Es un digito?", is_digit)

print("IV".isnumeric())


#replace -> Remplazr un texto a por un texto b

lista_compras="Leche, papel higenico, verduras, carnes, yogurt"

print(lista_compras.replace("papel higenico", "vino"))

#find -> encontrar / lo que hace es encontrar el indice de inicio de cierta cadena de texto 
print(lista_compras.find('papel'))


nueva_lista_compras="Leche, papel higenico, verduras, carnes , yogurt, leche"
print(nueva_lista_compras.rfind('Leche'))


print(nueva_lista_compras.count('leche'))


print("Hola mundo, que tal te va?". endswith('va?'))


#split()-> Este metodo retorna la lista de caracteres como un elemento de arreglo/lista



print("Ginio, Pedro, Rodrigo, Rodolfo, Jeriot". split(','))
