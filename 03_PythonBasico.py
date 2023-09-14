#================================
# Arturo Martínez Espinosa
#================================
# Matemática Algorítmica
# Patadigmas de Programación
# ESFM IPN Septiembre 2023
# ===============================

#============================================
# Listas
# Las listas pueden ser de objetos diferentes
#============================================
miprimeralista =[]    # Lista vacía
print (miprimeralista)

#============================================
# Llenado de la lista
#============================================
miprimeralista = [1,"Javier",1.34,"Bosco","Ángel","Abigail", True]
print(miprimeralista)

#=================================================
# list: hacer una lista
# range (i,j): secuencia de i hasta j-1
#=================================================
nums = list(range(1,61))

for i in nums:
    print(i)

#==========================================
# Incluír nuevos elementos en la lista
#==========================================

nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#========================================
# Quitar elementos de la lista
#========================================
nums.remove(61)
print(nums)

#=======================================
# Quitar elemento con índice i
#=======================================
i = 61
del nums[i]
print(nums)

#==================================
# Borrar la lista
#==================================
del nums

#=================================
# Sumar listas
#=================================
L1 = [1,2,3]
L2 = [4,5,6]
print (L1+L2)

#=========================================
# Llenado a mano
#=========================================
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#=======================================
# Generar una tupla con la lista
#=======================================
potencial = tuple(potencial)
print(potencial[100])

