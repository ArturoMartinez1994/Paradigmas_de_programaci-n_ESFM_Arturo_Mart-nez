#============================
# Arturo Martínez Espinosa
#============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#============================

#===========================================================
# Las colas (queues) son memorias compartidas entre procesos
#===========================================================
from multiprocessing import Process,Queue

def cubico(x,q):
    # Poner en la memoria compartida una tupla (x,x_cúbica)
    q.put((x,x*x*x))

#===================
# Código principal
#===================
if __name__ == "__main__":

    # q es una cola (memoria compartida)
    q = Queue()

    #======================================
    # Instanciar una lista de procesos
    #======================================
    procesos = [Process(target=cubico,args=(i,q)) for i in range(1,10)]

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    #========================================================================
    # Método get (les pido a los procesos que me den su resultado en la cola)
    # No nos da el resultado en orden hay que ponerle identificador
    #========================================================================
    resultado = [q.get() for p in procesos]

    print(resultado)
