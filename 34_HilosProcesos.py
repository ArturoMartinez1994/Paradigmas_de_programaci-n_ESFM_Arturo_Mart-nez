#===========================
# Arturo Martínez Espinosa
#===========================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#===========================

#===========================================================
# Módulos de hilos, procesos, sistema, matemáticas y tiempo
#===========================================================
from threading import Thread
from multiprocessing import Process
import os
import math
import time

#===========
# Función
#===========
def calc():
    for i in range(0,4000000):
        math.sqrt(i)

#================
# Lista de hilos
#================
threads = []

#============================
# Procesadores de mi máquina
#============================
cpus = os.cpu_count()
print("Número de procesadores: ",cpus)

#============================
# Inscribir hios en la lista
#============================
for i in range(cpus):
    print("registrando el hilo %d" %i)
    threads.append(Thread(target=calc))

start = time.time()
#=========================================
# Iniciar todos los hilos (son seriales)
#=========================================
for thread in threads:
    thread.start()

#===================================
# Esperar a que terminen los hilos
#===================================
for thread in threads:
    thread.join()

end = time.time()
#=====================
# Restar los tiempos
#=====================
print("Se tardó: ",end-start)

#====================
# Lista de procesos
#====================
procesos = []
for i in range (cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

#=================================
# Iniciar procesos (en paralelo)
#=================================
for proceso in procesos:
    proceso.start()

#====================
# Terminar procesos
#====================
for proceso in procesos:
    proceso.join()

end= time.time()
print("Se tardó: ",end-start)
