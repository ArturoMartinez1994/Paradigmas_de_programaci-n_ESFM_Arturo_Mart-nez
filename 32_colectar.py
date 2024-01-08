#============================
# Arturo Martínez Espinosa
#============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Diciembre 2023
#============================
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# un dato
data = (rank+1)**2
#==============================================
# Manden sus datos al proceso root=0 (en orden)
#==============================================
datas = comm.gather(data, root=0)

#===============================
# Asegurarse que todo funcione
#===============================
if rank == 0:
    for i in range (size) :
        assert datas[i] == (i+1)**2
else:
    assert datas is None
print(datas)

#============================
# Ahora más rápido con numpy
#============================
n = 10
#==========================================
# Arreglo de ceros de tamaño n
# sumado con un escalar (en cada entrada)
#==========================================
sendarray = numpy.zeros(n,dtype='i')+rank
recvarray = None
if rank == 0:
    #=======================================
    # Matriz vacía de tamaño procesos * n
    # dtype es el tipo de dato (i) es entero
    #=======================================
    recvarray = numpy.empty([size, n], dtype='i')
#==============================
# Gather es rápido para numpy
# enviar datos al proceso root
#==============================
comm.Gather(sendarray, recvarray, root=0)
if rank == 0:
    for i in range(size):
        #=========================================================
        # Revisar por fila la matriz
        # : significa todos los elementos de es dimensión
        # allclose es un método de numpy que compara los elementos
        #=========================================================
        assert numpy.allclose(recvarray[i,:], i)
print(recvarray)

