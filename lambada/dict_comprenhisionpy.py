word="aaaabbcccxa"

dict_palabra ={letra: word.count(letra) for letra in set(word)}
print(dict_palabra)


texto ="Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres. "

lista_palabra = texto.replace(",","").replace(",","").split()
dict_palabras1= {palabra: lista_palabra.count(palabra) for palabra in set(lista_palabra)}
print(dict_palabras1)




students =["Rodrigo","Rodolfo","Jeriot","Marco"]
nota=[13,17,17,18]
objects_zip = zip(students,nota)
print(objects_zip, type(objects_zip))



students_capps= {estudiante: nota for estudiante, nota in objects_zip} 
print(students_capps, type(students))