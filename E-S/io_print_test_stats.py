import time


if __name__ == '__main__':
    base_str = "*"

    print("[*] Iniciando evaluacion de print")
    contenido = "iteracion,promedio,maximo,minimo,medianta\n"
    for idx in range(20):
        print(f"[*] Corriendo iteracion {idx + 1}")
        res = list()

        for i in range(200):
            full_str = base_str * (i + 1)
            
            inicio = time.perf_counter()
            print(full_str)
            fin = time.perf_counter()
            res.append(fin - inicio)

        promedio = sum(res) / len(res)
        maximo = max(res)
        minimo = min(res)
        res.sort()
        mediana = res[int(len(res) / 2)]
        fila = f"{idx + 1},{promedio},{maximo},{minimo},{mediana}\n"
        contenido += fila
    print("[*] Pruebas terminadas procediendo a escribir en archivo")

    contenido = contenido[:-1]
    with open("print_stats.csv", "w+") as f:
        f.write(contenido)
    
    print("[*] Escritura completa, terminando programa...")
