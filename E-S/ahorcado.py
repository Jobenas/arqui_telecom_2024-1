from random import randint
from typing import Union


palabras = ["arquitectura", "computadoras", "universidad", "alumnos", "clases", "telecomunicaciones"] 
palabra = palabras[randint(0, len(palabras) - 1)]
intentos = 5
palabra_lista = ["_"] * len(palabra)


def busca_letra(p: str, l: str, p_lista: list[str]) -> Union[list[str], bool]:
    palabra_encontrada = False
    for idx in range(len(palabra)):
        if l == p[idx]:
            p_lista[idx] = l
            palabra_encontrada = True

    return p_lista, palabra_encontrada


if __name__ == '__main__':
    while True:
        print(f"{''.join(palabra_lista)}\n\nCantidad de intentos: {intentos}\n")
        letra = input("Por favor ingrese una letra: ")
        while len(letra) != 1:
            letra = input("Por favor ingrese una letra: ")

        palabra_lista, encontrada = busca_letra(palabra, letra, palabra_lista)

        if not encontrada:
            intentos -= 1
            print("Letra ingresada no pertenece a la palabra")

        if intentos == 0:
            print("Lo siento, ha perdido el juego")
            exit(0)

        if not "_" in palabra_lista:
            print(f"Felicitaciones, ha encontrado la palabra: {palabra}")
            exit(0)
