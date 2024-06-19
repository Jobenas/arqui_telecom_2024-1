import time
from threading import Thread

N = 500_000_000


def count(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    t1 = Thread(target=count, args=(N // 2, ))
    t2 = Thread(target=count, args=(N // 2, ))
    print("Inicio del programa")
    inicio = time.perf_counter()
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.8f} segundos") 
