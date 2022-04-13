#funcion es un conjunto de instrucciones que realizan un proceso
#su principal ventaja es que nos ayudan a evitar codigo repetido.


def saludar():
    print("javier")
    print("catalan")
    return "hola"

print(saludar())


def evaluarSueldoMinimo(sueldo):
    if sueldo >= 3000:
        print ("cumples con el sueldo")
    else:
        print("ganas menos del sueldo minimo")

evaluarSueldoMinimo(3000)