import time

N = 100_000_000


def count(n):
    while n > 0:
        n -= 1
    

if __name__ == '__main__':
    print("Inicio del programa")
    inicio = time.perf_counter()
    count(N)
    fin = time.perf_counter()
    print("Final de cuenta")

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.8f} segundos")
