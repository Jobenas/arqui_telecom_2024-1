from threading import Thread
import time


def count(idx: int):
    print(f"[{idx}] Uno")
    time.sleep(1)
    print(f"[{idx}] Dos")


def main():
    threads = list()

    for i in range(3):
        t = Thread(target=count, args=(i, ))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    
if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {(fin - inicio):0.8f} segundos")
