from threading import Thread
import time


def count():
    print("Uno")
    time.sleep(1)
    print("Dos")


def main():
    threads = list()

    for _ in range(3):
        t = Thread(target=count)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    
if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {(fin - inicio):0.8f} segundos")
