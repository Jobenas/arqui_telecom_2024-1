from itertools import repeat
from multiprocessing import cpu_count, Pool
import numpy as np
import time

M = 5000
N = 5000


def mult_vector(x: list[np.int32], y: list[np.int32]) -> np.int32:
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]

    return suma


if __name__ == '__main__':
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    processes = list()
    inicio = time.perf_counter()

    args = zip(mat_M, repeat(vector_A))

    with Pool(processes=cpu_count()) as p:
        resultado = p.starmap(mult_vector, args)

    fin = time.perf_counter()

    print(f"Tiempo de ejecucion asincrono: {(fin - inicio):0.2f} segundos")

        
