# Raise: sirve para lanzar (de forma intencional) excepciones en python.

def evaluarNota(nota):
    if nota < 0:
        #raise ZeroDivisionError("Este mensaje es personalizable")
        raise ValueError("valor incorrecto..")
    elif nota >= 16:
        print("Exelente")
    elif nota >= 11:
        print("aprovado")
    else:
        print("Desaprobado")

evaluarNota(-   1)

print("Este es el fin de mi programa.")