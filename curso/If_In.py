print("--Cursos--")
print("Matemetica -Biologia - Lenguaje - Ciencia")

curso = input("Ingrese el curso deseado: ")

print(curso)

if curso in ("Matematica", "Biologia","Lenguaje", "Ciencia"):
    print("Curso {0} seleccionado".format(curso))
else:
    print("No existe ese curso")