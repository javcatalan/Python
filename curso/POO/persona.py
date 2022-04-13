"""
¿En que consiste la Programacion Orientada a Objetos?
- En trasladar la naturaleza de los objetos de la vida real a codigo
de programacion (en algún lenguaje de programacion, como python)

Los objetos de la realidad tienen caracteristicas (atributos o propiedades)
 y funciionalidades o comportamientos (funciones o metodos)

 Ventajas:
 - Modularizacion (division en pequeñas partes) de un programa completo
 - Codigo fuente muy reutilizable
 - Codigo fuente mas facil de incrementar en el futuro y mantener.
 - Si existe un fallo en una pequeña parte del codigo el programa completo
 no debe fallar necesariamente. Ademas, es mas facil de corregir esos fallos.
 - Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto
"""

class Persona():
    # Propiedades, caracteristicas o abributos
    apellidos= ""
    nombres = ""
    edad = 0
    despierta = False

    # Funcionalidades:
    def despertar(self):
        # self: parametro que hace referencia a la instancia perteneciente a la clase
        self.despierta = True
        print("buen dia.")


persona1 = Persona()
persona1.apellidos = "Garcia Fuentes"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos = "Paz Torres"
print(persona2.apellidos)
persona2.despertar()
print(persona2.despierta)