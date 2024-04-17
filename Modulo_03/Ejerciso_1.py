"""

"""

condicional = True

lista_de_numeros=[]

while condicional:
    try:
        texto_entrada=input("Ingrese un numero: ")
        if texto_entrada.upper() == 'FIN':
            condicional=False
        else:
            numero=int(texto_entrada)
            lista_de_numeros.append(numero)        
    except ValueError:
        print("Ingrese un dato numerico")

print(f"""
Menor numero encontrado
Mayor numero encontrado

""")