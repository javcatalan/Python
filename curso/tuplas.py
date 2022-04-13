"""
tupla: es una estructura de datos propia de python que puede almacenar diferentes valorss,
son inmutables: no cambian una vez inicializadas
"""

tupla = (1,2,3)
print(tupla)
tupla2 = (7, "oscar", True, 450.5, 850 + 7j)
print(tupla2)
tupla3 = (9, 93, (4, 9, 6))
print(tupla3)
print(tupla2[1])
#tupla2[1] = "kladsa"
print(tupla2[-1])
print(tupla2[0:4])
print(tupla2[-2])

a, b, c, =tupla
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3
print(tuplaFinal)

print(tuplaFinal.count(3))
print(tuplaFinal.index(3))
