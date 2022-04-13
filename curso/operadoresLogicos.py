# AND: equivalente a Y si ademas
# OR: o sino
# not -> negacion

distancia = 400
numeroHermanos = 3
salarioPadres = 3500

tieneBeneficio = False
if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
    tieneBeneficio = True

print(not tieneBeneficio)

if (5>3) and (8>6):
    print("verdadero")
else:
    print("es mentira")