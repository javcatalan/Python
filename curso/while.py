#while estructura repetitiva que nos permite realizar multiples iteraciones
#basandonos en el resultado de una expresion logica que puede tener
# como resultado un valor True o False

indice = 1

while indice < 10:
    print("valor actual: {0}".format(indice))
    indice = indice + 1

print("hemos terminado el bucle while")

inicio = 2

while inicio <= 100:
    print("numero par: {0}".format(inicio))
    inicio += 2
print("hemos terminado el bucle while")
