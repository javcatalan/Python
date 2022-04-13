#diccionarios: son estructuras de datos que nos permiten almacenar distintos valores
#es que los datos se almacenan en una clave unica se relacionan en na clave: valor
#los elementos almacenados estan en desorde, el orden es indeferente en el almacenamiento

miDiccionaro = {"españa":"madrid","peru":"lima","alemania":"berlin"}
print(miDiccionaro["peru"])
print(miDiccionaro)

miDiccionaro["venezuela"]= "caracas"
print(miDiccionaro)

miDiccionaro["españa"]= "barcelona"
print(miDiccionaro)

del miDiccionaro["españa"]
print(miDiccionaro)

dic2 = {"javier":"catalan", 25: True, "sueldo":13121}
print(dic2)

llaves = ("españa","francia","inglaterra")
print(llaves)
dicPaises = {llaves[0]: "madrid",llaves[1]:"paris",llaves[2]:"londres"}
print(dicPaises)

datosPersonales = {"apellido":"garcia","years":{1:2000, 2:2001, 3:2002, 4:2003}}
print(datosPersonales)
print(datosPersonales["years"])

print(datosPersonales.get("apellido","oscar"))

print(datosPersonales.keys())
valores= list(datosPersonales.values())
print(valores)
valores= tuple(datosPersonales.values())
print(datosPersonales.values())