from multiprocessing import Pool
import time

proc = 4
tareas = proc * 4


def potencia(n: int, div: int = tareas) -> int:
    pot = 1
    rango = n // div

    for _ in range(rango):
        pot = pot * n

    return pot


if __name__ == '__main__':
    args = [100_000] * tareas

    inicio = time.perf_counter()
    
    p = Pool(processes=proc)
    pl = p.map(potencia, args)
    p.close()
    p.join()

    pot_total = 1
    for i in range(len(pl)):
        pot_total *= pl[i]

    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.3f} segundos")
