from datetime import datetime
from random import randint
from typing import Union


intentos = 5

l_correctas_lista = list()
l_incorrectas_lista = list()
repeticiones = 0

def carga_lista_palabras() -> list[str]:
    with open('palabras.arqui', 'r') as f:
        contenido = f.read()
    
    l_palabras = contenido.split("\n")
    return l_palabras


def selecciona_palabra(lista_palabras: list[str]) -> str:
    p = lista_palabras[randint(0, len(lista_palabras) - 1)]

    return p


def busca_letra(p: str, l: str, p_lista: list[str]) -> Union[list[str], bool]:
    palabra_encontrada = False
    for idx in range(len(p)):
        if l == p[idx]:
            p_lista[idx] = l
            palabra_encontrada = True

    return p_lista, palabra_encontrada


def registra_stat(reps: int, p: str, l_incorrectas: list[str], res: bool, tiempo: int):
    fila = f"{p},{';'.join(l_incorrectas) if len(l_incorrectas) > 0 else 'Ninguna'},{'victoria' if res else 'derrota'},{reps},{tiempo}\n"
    with open('stats.csv', 'r') as f:
        contenido = f.read()
    
    contenido += fila

    with open('stats.csv', 'w+') as f:
        f.write(contenido)


if __name__ == '__main__':
    print("Iniciando juego, cargando configuracion...")

    palabras = carga_lista_palabras()
    palabra = selecciona_palabra(palabras)
    palabra_lista = ["_"] * len(palabra)
    
    inicio = datetime.now()
    while True:
        print(f"{''.join(palabra_lista)}\n\nCantidad de intentos: {intentos}\t\tLetras incorrectas: {', '.join(l_incorrectas_lista)}\n")
        letra = input("Por favor ingrese una letra: ")
        while len(letra) != 1:
            letra = input("Por favor ingrese una letra: ")

        if letra in l_correctas_lista or letra in l_incorrectas_lista:
            repeticiones += 1
            print("Letra ya ingresada, intente nuevamente")
            continue

        palabra_lista, encontrada = busca_letra(palabra, letra, palabra_lista)

        if not encontrada:
            intentos -= 1
            print("Letra ingresada no pertenece a la palabra")
            l_incorrectas_lista.append(letra)
        else:
            l_correctas_lista.append(letra)

        if intentos == 0:
            fin = datetime.now()
            t_secs = (fin - inicio).total_seconds()
            registra_stat(repeticiones, palabra, l_incorrectas_lista, False, t_secs)
            print("Lo siento, ha perdido el juego")
            exit(0)

        if not "_" in palabra_lista:
            fin = datetime.now()
            t_secs = (fin - inicio).total_seconds()
            registra_stat(repeticiones, palabra, l_incorrectas_lista, True, t_secs)
            print(f"Felicitaciones, ha encontrado la palabra: {palabra}")
            exit(0)
