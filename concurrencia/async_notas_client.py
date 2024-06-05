import asyncio

SOCKET_BUFFER = 1024

async def send(writer, msg):
    print(f"Enviando mensaje: {msg}")
    msg_bytes = msg.encode("utf-8")
    writer.write(msg_bytes)
    await writer.drain()


async def recv(reader):
    print("Esperando respuesta")
    result_bytes = await reader.read(SOCKET_BUFFER)
    print(f"recibi en bytes {result_bytes}")
    result = result_bytes.decode("utf-8")

    return result


async def client(server_ip: str, server_port: int, msg: str):
    server_address = (server_ip, server_port)
    print(f"Conectando a {server_address[0]}:{server_address[1]}")
    reader, writer = await asyncio.open_connection(server_address[0], server_address[1])
    print("Conectado")
    await send(writer, msg)
    
    res = await recv(reader)

    print("cerrando la conexion")
    writer.close()
    await writer.wait_closed()

    return res
