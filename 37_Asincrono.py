#============================
# Arturo Martínez Espinosa
#============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#============================
import multiprocessing as mp
import numpy as np
import time

def func(i, param1, param2, param3):
    # calcula un poinomio
    result = param1**2 +param2 +param3
    # se hace tonta 2 segundos
    time.sleep(2)
    return (i,result)

def resultado(result):
    # se inscriben en lista global
    global results
    results.append(result)

#=======================
# Programa principal
#=======================
if __name__ == "__main__":

    # Matriz de 10x3 números al azar
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    # Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())

    # loop de primera dimensión del arreglo
    for i in range(0, params.shape[0]):
        #=======================================================
        # Correr asincrónicamente my_function con argumentos args
        # y cuando termine correr resultado
        #========================================================
        pool.apply_async(func, args = (i,params[i,0], params[i,1], params[i,2]), callback=resultado)

    #===============================
    # Cerrar el grupo de procesos
    #===============================
    pool.close()
    # Esperar que termine el grupo
    pool.join()

    print("Tiempo en paralelo = ", time.time()-ts)
    print(results)


