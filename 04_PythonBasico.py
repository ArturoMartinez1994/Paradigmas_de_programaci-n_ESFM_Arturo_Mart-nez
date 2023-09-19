#=========================================
# Arturo Martínez Espinosa
#=========================================
# Matemática Algorítmica
# Paradigmas de Programación
# ESFM IPN Septiembre 2023
#=========================================

#=========================================
# Conjunto den python
#=========================================
even_nums ={2,4,6,8,10}  # conjunto de números pares 
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} #conjunto de diferentes objetos
print (emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print (nums)

#============================================
# Convertir secuencia a conjunto
# No lo genera en orden
#============================================
s = set('Hola')
print(s)
s = set((1,2,3,4,5)) # tupla a conjnto
print(s)

#===============================================
# De diccionario a conjunto : conjunto de llaves
#===============================================
d = {1:'uno', 2: 'dos'}
s = set(d)
print(s)

s.aad(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 # Unión
print (su)

si = s1&s2 # Intersección
print (si)

sr = s1-s2 # Diferencia de conjuntos
print (sr)

sp = s2-s1
print(sp)

ss = s1^s2 # Diferencia simétrica
print (ss)

#==============================
# Uso de diccionarios
#==============================
capitales = {"USA":"Washington D.C.","France":"Paris","India":"New Delhi"}
print(capitales)

#==============================
# llave:valor
#==============================
# diccionario vacío
d = {}

# Llave entera, valor string
numeros={1:"uno",2:"dos", 3:"tres"}

#Llave real, valor string
decimales={1.5:"uno y medio", 2.5: "dos y medio", 3.5:"tes y medio"}

#Llave tupla, valor string
cosas={("Parker","Reynolds","Camlin"):"pluma",("LG","Whirlpool","Samsung"): "Refrigerador"}

#Llave string, valor int
romanos = {'I':1, 'II' :2, 'III' :3, 'IV' :4, 'V' :5}
print(romanos)
print(romanos["I"])

print(capitales.get("India"))
print(capitales.get("india"))

#Reportat llave y valor
for k in capitales:
    print("Key = " + k + ", Value = " + capitales[k])

#Nuevo dato para el diccionario
capitales["Mexico"] = "CDMX"
print (capitales)

# Borrar dato del diccionario
del capitales ["Mexico"]
print(capitales)

# Borrar todo el diccionario
del capitales

# Reportar llaves
print (romanos.key())

#Reportar valores
print(romanos.values())

#Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" not in romanos)


