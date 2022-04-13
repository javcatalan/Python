#Excepcion: Error en tiempo de ejecucion ( durante le ejecucion de dicho programa)

numero1 = 20
numero2 = 2

#print("La division de {0} entre {1} es: {2}".format(numero1, numero2(numero1/numero2)))

try:
    resultado = numero1/numero2
    print(resultado)
#except:
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Yo siempre aparezco.")

print("Aqui termina mi programa")