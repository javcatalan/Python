 #  Polimorfismo (poli => muchas / morfos: formas)

class Estudiante():

     def describir(self):
         print("Soy un buen estudiante")

class Docente():

     def describir(self):
         print("soy un buen estudiante")

class Trabajador():

    def describir(self):
        print("soy un buen trabajador")

def describirPersona(persona):
    persona.describir()

doc1=Trabajador()
describirPersona(doc1)

dec2 = Estudiante()
describirPersona(dec2)
