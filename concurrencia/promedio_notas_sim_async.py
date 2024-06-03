import asyncio
from random import randint, random


async def obten_nota(codigo: str) -> float:
    print(f"Procesando notas para {codigo}")

    await asyncio.sleep(randint(1, 4))

    nota_final = random() * 20

    return nota_final


async def main():
    codigo_base = 20240001
    codigos = [str(codigo_base + idx) for idx in range(10)]
    notas_finales = await asyncio.gather(*(obten_nota(codigo) for codigo in codigos))

    return notas_finales


if __name__ == "__main__":
    notas = asyncio.run(main())

    promedio_nota_final = sum(notas) / len(notas)

    print(f"El promedio de notas finales es: {promedio_nota_final:0.2f}")
