#============================
# Arturo Martínez Espinosa
#============================
# Paradigmas de Progaramación
# Matemática Algoritmica
# ESFM IPN Octubre 2023
#============================

#=========================================
# Uso de reducciones (colapsar resultados)
#=========================================

#================================================
# Multiplicación de todos los números en la lista
#================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#==============
# Función x*y
#==============
multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#==========================================================
# Reduce le aplica la función por pares a los resultados y
# el siguiente elemento comenzando con los dos primeros
# elementos.
#==========================================================

