#cuando indicamos un * delante del parametro de una funcion,
#estamos indicando que se va a recibir un numero indeterminado
#de parametros. Ademas, esos parametros se recibiran en forma de tupla
"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng
"""
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        yield from leng


lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "Javascript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))