import time


def potencia(n: int) -> int:
    pot = 1

    for _ in range(n):
        pot = pot * n
    
    return pot


if __name__ == '__main__':
    print("Inicio del programa")
    inicio = time.perf_counter()
    potencia(100_000)
    fin = time.perf_counter()
    print("Final de potencia")

    print(f"Tiempo total de ejecucion: {(fin - inicio):0.3f} segundos")
