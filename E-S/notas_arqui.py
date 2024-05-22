import time


if __name__ == '__main__':
    codigo = "20240050"

    inicio_es = time.perf_counter()
    with open("notas_arqui.csv", "r") as f:
        contenido = f.read()
    fin_es = time.perf_counter()

    contenido_lista = contenido.split("\n")
    notas = ""
    for fila in contenido_lista:
        items = fila.split(",")
        if items[0] == codigo:
            notas = fila
            break
    
    inicio_cpu = time.perf_counter()
    notas = notas.split(",")
    notas = [int(v) for v in notas]
    nota_lab = sum(notas[1:15]) / len(notas[1:15])
    e1 = notas[15]
    e2 = notas[16]

    nota_final = (nota_lab * 0.5) + (e1 * 0.25) + (e2 * 0.25)
    fin_cpu = time.perf_counter()

    print(f"Nota final: {nota_final}, tiempo en E/S {fin_es - inicio_es} segundos - tiempo en CPU {fin_cpu - inicio_cpu} segundos")
