#===========================
# Arturo Martínez Espinosa
#===========================
# Paradigmas de programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#===========================

#==============================================
# Uso de MPI Optimizado para cálculos numéricos
#==============================================
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):

        #=====================================
        # Lista común
        #=====================================
        self.x = [i for i in range(rank*10)]
        self.p = "vengo del proceso "+str(rank)

        #================================
        # Arreglo de numpy (optimizado)
        #================================
        self.xx = np.array([float(x+rank) for x in range(10)])
        self.pp = "vengo del proceso "+str(rank)

#=========================
# Programa principal
#=========================
if __name__== "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0
    
    #======================
    # Envío no bloqueante
    #======================
    comm.isend(s, dest=dst)

    #==================================
    # Recibir no bloqueante con espera
    # req: request (petición)
    #==================================
    req = comm.irecv(source=src)
    a = req.wait()

    print("Soy el proceso ", rank ,", el resultado es ", len(a.x), a.p)

    #================================
    # Arreglo de numpy para enviar
    #================================
    m = s.xx

    #=====================================
    # Isend Irecv son para comunicación
    # no bloqueante de arreglos de numpy
    #=====================================
    comm.Isend(m, dest=dst)

    #======================================
    # Arreglo vacío para recibir
    # con dimensión 10 y tipo de datos
    # float64 (doble precisión)
    #======================================
    aa = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(aa, source=src)
    req.Wait()

    print("Soy el proceso ", rank ,", el resultado es ",aa)

