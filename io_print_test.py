import time


if __name__ == '__main__':
    base_str = "*"
    res = list()

    for i in range(200):
        full_str = base_str * (i + 1)
        
        inicio = time.perf_counter()
        print(full_str)
        fin = time.perf_counter()

        print(f"Tiempo de ejecucion para {i + 1} caracteres -> {fin - inicio} segundos")
        res.append(fin - inicio)

    promedio = sum(res) / len(res)
    maximo = max(res)
    minimo = min(res)
    res.sort()
    mediana = res[int(len(res) / 2)]
    print("**************************************************")
    print(f"Parametros estadisticos:\npromedio\t->\t{promedio}\nmaximo\t->\t{maximo}\nminimo\t->\t{minimo}\nmediana\t->\t{mediana}")
    print("**************************************************")
    
