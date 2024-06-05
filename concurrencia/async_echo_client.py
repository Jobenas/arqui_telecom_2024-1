import asyncio


async def send(writer, msg):
    print(f"Enviando mensaje: {msg}")
    msg_bytes = msg.encode("utf-8")
    writer.write(msg_bytes)
    await writer.drain()


async def recv(reader):
    print("Esperando respuesta")
    result_bytes = await reader.readline()
    print(f"recibi en bytes {result_bytes}")
    result = result_bytes.decode("utf-8")

    return result


async def client(idx):
    server_address = ("localhost", 5500)
    print(f"Conectando a {server_address[0]}:{server_address[1]}")
    reader, writer = await asyncio.open_connection(server_address[0], server_address[1])
    print("Conectado")
    await send(writer, f"Hola mundo! desde cliente {idx}")
    
    res = await recv(reader)

    print("cerrando la conexion")
    writer.close()
    await writer.wait_closed()

    return res


async def main():
    res = await asyncio.gather(*(client(idx + 1) for idx in range(10)))

    return res


if __name__ == '__main__':
    mensajes = asyncio.run(main())

    print(f"Cliente recibio el mensaje: {mensajes[0]}")

