#==============================
# Arturo Martínez Espinosa
#==============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#==============================

#==========================================================
# Ejemplo de comunicación bloqueada a un arreglo compartido
#==========================================================
from multiprocessing import Process, Array, Value, Lock
import time

#==========================================================
# Hay dos formas de usar los candados para evitar
# que dos procesos escriban en el mismo lugar
#==========================================================
def sumale100_1(numeros,candado):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numeros)):
            #=====================================================
            # lo que esté dentro de con candado no puede accederse
            # desde oro proceso al mismo tiempo
            #=====================================================
            with candado:
              numeros[i] += 1

def sumale100_2(numero,candano):
    for i in range(100):
        time.sleep(0.01)
        # Poner el candado
        candado.acquire()
        # Hacer la operación
        numero.value += 1
        # Quitar el candado
        candado.release()

if __name__ == "__main__":
    #==================================================
    # Candado para evitar que dos procesos se empalem
    #==================================================
    candado = Lock()

    # Arreglo compartido entre los procesos, 'd' es doble precisión
    numeros_compartidos = Array('d', [0.0, 100.0, 200.0])

    # : quiere decir todos los elementos
    print("Al principio vale = ", numeros_compartidos[:])

    p1 = Process(target=sumale100_1, args=(numeros_compartidos,candado))
    p2 = Process(target=sumale100_1, args=(numeros_compartidos,candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Al final vale = ", numeros_compartidos[:])

    # Entero compartido
    numero_compartido = Value('i', 0)
    print("Al principio vale = ", numero_compartido.value)
    p1 = Process(target=sumale100_2, args=(numero_compartido,candado))
    p2 = Process(target=sumale100_2, args=(numero_compartido,candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Al final vale = ", numero_compartido.value)
