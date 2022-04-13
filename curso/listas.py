#listas: son extructuras de datos que nos permiten almacenar datos
#son equivalentes a los array en otros lenguahes de programacion
#son estructuras dinamicas, se pueden mutar

lista1 = ["oscar", 25, 96.5,"True", 654]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])

print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("jfalsd")
print(lista1)

lista1.insert(4, "guate")
print(lista1)

lista1.extend(["javier", 54, False])
print(lista1)

print(lista1.index("javier"))

lista1.remove(25)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["jlsadf", "ijasd"]
lista3 = lista1+lista2
print(lista3)

print(lista2 * 4)

print("javier" in lista1)