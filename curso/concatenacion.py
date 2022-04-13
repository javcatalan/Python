texto1 = "hola"
texto2 = "catalan"
textofinal = texto1 + " " + texto2
print(textofinal)

print("el saludo es: %s %s" % (texto1, texto2))

saludofinal = "saludo: {0} {1}".format(texto1,texto2)
print(saludofinal)

saludofinal2 = "saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludofinal2)