#Break: permite salir del un bucle cuando se cumple una condeicion

for numero in range(1,7):
    if numero == 3:
        break #descanso o interrupcion
    print("El numero es: {0}".format(numero))

print("bucle terminado")

#Continue : omite una parte del bucle cuando se cumple una condicion y
# continua con el resto

for numero in range(2,9):
    if numero == 6:
        continue
    print("el numero es: {0}".format(numero))
print("done")

#Pass permite contunuar con una sentencia o funcion que ya tiene onaun no tiene uñ
#bloque de codigo util

for numero in range(2,8):
    if numero <=5:
        #aqui no pasa nada y el bucle sigue trabajando
        pass
    else:
        print("el siguiente valor es 6")
    print("el numero es {0}".format(numero))

print("fin del bucle")

def funcionSininplementar():
    pass

