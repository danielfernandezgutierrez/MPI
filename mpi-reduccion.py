from mpi4py import MPI
import random
#inicializacion de Entorno MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Se crea un conjunto de datos distribuido 
#a:numero de datos por proceso
def suma_local( a):
    data = [random.randint(1, 100) for i in range(a)]
    print(data)
    print(sum(data))
    return sum(data)

#Reducir la suma local para obtener la global
global_suma = comm.reduce(suma_local(10), op=MPI.SUM, root=0)

#El proceso 0 imprime el resultado
if rank== 0:
    print(f"La suma total es: {global_suma}")

#Finalizar entorno MPI
MPI.Finalize()
