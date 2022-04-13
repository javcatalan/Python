"""
Paquetes:
Directorios (carpetes) donde se almacenan modulos relacionados entres si.

¿Pará que sirven?
para organizar mejor el codigo y poder reutilizarlo mejor (modularizanion y reutilizacion)

¿Como se crea un paquete?
Crear una carpeta o directorio con un archivo dentro llamado __init__.py

Lo que hace  __ init__.py es "convertir" un directorio en un modulo (paquete)
que contiene otros modulos, y esto lo hace para poder importarlos..
"""

from paquete1.funcionesNumericas import *
from paquete1.funcionesCadenas import contarLetras

print(multiplicar(6,8))
print(contarLetras("jfjajfdlahggdfgsñdl"))
