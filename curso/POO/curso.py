"""
class Curso():
    nombre= "matematicas"
    creditos = 5
    profesion = "Ingenieria civil"
    """

#estado inicial del objeto
class Curso():
    def __init__(self, nom,cre,pro):
        self.nombre= nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion="presencial"


    def mostrarDatos(self):
        dat= "Nombre: {0} / Creditos: {1} / Modelo de imparticion {2}"
        print(dat.format(self.nombre,self.creditos,self.__imparticion))
        docenteAdignado=self.__verificarDocente()
        if docenteAdignado:
            print("existe docente adignado.")
        else:
            print("no es necesario asignar un docente..")

    def __verificarDocente(self):
        print("verificando si exoste docente asignado")
        if self.__imparticion == "presencial":
            return True
        else:
            return False
}
    #tostring()
    def __str__(self):
        texto = "nombre: {0} - Creditos: {1}"
        return texto.format(self.nombre,self.creditos)

curso1 = Curso("matecaticas",5,"ingenieria civil")
print(curso1)
curso1.mostrarDatos()

curso2 = Curso("historia",8,"historiologia")
print(curso2.creditos)