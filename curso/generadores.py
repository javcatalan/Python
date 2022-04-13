#Generadores: Permiten extraer valores de una funcion y almacenarlo(de uno en uno)
#en objetos iterables (que se pueden recorrer)
# sin la necesidad de almacenar TODOS A LA VEZ en la memoria RAM

"""
def generaMultiplos7(limite):
    numero = 1
    listaNumeros = []

    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros #retornando toda la lista creada

print(generaMultiplos7(10))
"""

def generadorMultiplos8(limite):
    numero = 1

    while numero <= limite:
        yield numero * 8 #Ceder. la intruccion YIELD genera un objeto iterable
        numero = numero + 1

obtieneMultiplos8 = generadorMultiplos8(10)

#print(obtieneMultiplos8)
#for n in obtieneMultiplos8:
#   print(n)

#next() : nos retorna el siguiente elemento de un objet iterable

print(next(obtieneMultiplos8))
print("aca hay 300 lineas de codigo..")
print(next(obtieneMultiplos8))
print("aca hay 100 lineas de codigo..")
print(next(obtieneMultiplos8))
print("....")

#Son mas eficientes que las funciones tradiciionales.
#Muy utiles con las listas de valores infinitos
#Entre llamada y llamada, el objeto iterable entra en un estyado de pausa (suspencion)
