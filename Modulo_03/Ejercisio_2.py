condicional=True
lista_de_numeros=[]
contador_numeros=0
suma=0
while condicional:
    try:
        texto_entrada=input("Ingrese un numero: ")
        if texto_entrada.upper() =='FIN':
            condicional=False
        else:
            numero=float(texto_entrada)
            contador_numeros=contador_numeros+1
            suma=suma+numero
            lista_de_numeros.append(numero)
    except ValueError:
        print("Debe ser ingresado un valor numerico")

print(f"""
1. La suma de los numeros : {suma}
2. EL total de numeros ingresados: {contador_numeros}

""")