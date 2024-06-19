from multiprocessing import Process
import time

N = 100_000_000


def count(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    n_processes = [2, 4, 8, 16, 32, 64]

    for n_process in n_processes:
        print(f"Iniciando {n_process} procesos")
        processes = list()

        for _ in range(n_process):
            p = Process(target=count, args=(N // n_process, ))
            processes.append(p)

        print("Inicio del programa")
        inicio = time.perf_counter()

        for p in processes:
            p.start()
        
        for p in processes:
            p.join()

        fin = time.perf_counter()

        print(f"Tiempo total de ejecucion para {n_process} procesos: {(fin - inicio):0.8f} segundos")

