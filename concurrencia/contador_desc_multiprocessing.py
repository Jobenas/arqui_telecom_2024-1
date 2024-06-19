from multiprocessing import Process
import time

N = 100_000_000


def count(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    p1 = Process(target=count, args=(N // 2, ))
    p2 = Process(target=count, args=(N // 2, ))

    print("Inicio del programa")
    inicio = time.perf_counter()

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.8f} segundos")

