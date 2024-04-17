lista_1 = ["1","2","3","4"]
obj_map= list(map(float,lista_1))
print(obj_map, type(obj_map), type(obj_map[0]))


lista_2 = [[1000,21,100,1],[2,3],[-21,-20],[21212,4,3]]
lista_2_map=tuple(map(min,lista_2))	
print(lista_2_map)


lista_3 = range(0,10,3)
lista_3_mapeado = list(map(lambda n: n+200, lista_3))
print(lista_3_mapeado)