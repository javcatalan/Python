class Persona():

    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidoMaterno, self.apellidoPaterno, self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):

    def __init__(self, apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom)
        self.profesion=pro


    def datos(self):
        super().datos()
        print("Profecion: {0}".format(self.profesion))


#estu1=Estudiante("Torres","lopez","juan","ingenieria civil")
estu1=Persona("Torres","lopez","juan")
#print(estu1.mostrarNombreCompleto())
#print(estu1.profesion)
#estu1.datos()
print(isinstance(estu1,Persona))