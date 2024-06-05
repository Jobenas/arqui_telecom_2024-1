import asyncio
import json

from async_notas_client import client


async def main():
    codigo_base = 20240001
    mensajes = [{"id": idx, "codigo": f"{codigo_base + idx}", "modo": "servidor"} for idx in range(10)]
    notas_finales_resp = await asyncio.gather(*(client("localhost", 5000, json.dumps(mensaje)) for mensaje in mensajes))

    notas_finales = list()
    for nota_json in notas_finales_resp:
        nota_msg = json.loads(nota_json)
        if nota_msg["estado"] == "exito":
            notas_finales.append(nota_msg["nota"])
        else:
            continue

    return notas_finales


if __name__ == "__main__":
    notas = asyncio.run(main())

    promedio_nota_final = sum(notas) / len(notas)

    print(f"El promedio de notas finales es: {promedio_nota_final:0.2f}")
