import json
import socket
import time

SOCK_BUFFER = 1024


def captura_tiempo(msg: dict) -> list[float]:
    tiempos = list()
    for i in range(10):
        print(f"[*] Realizando iteración {i + 1}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("localhost", 5000)

        print(f"[*] Conectando a servidor en {server_address[0]}:{server_address[1]}")

        sock.connect(server_address)
            
        msg_str = json.dumps(msg)

        print(f"[*] Preparándome para enviar {msg_str}")
        msg_bytes = msg_str.encode("utf-8")
        inicio = time.perf_counter()
        sock.sendall(msg_bytes)
        data = sock.recv(SOCK_BUFFER)
        fin = time.perf_counter()

        print(f"[!] Recibí: {data}")

        print(f"[*] Terminando operación, cerrando el socket")

        sock.close()
        tiempos.append(fin - inicio)

    return tiempos


if __name__ == '__main__':

    msg_cliente = {"codigo": "20240100", "modo": "cliente"}
    msg_servidor = {"codigo": "20240100", "modo": "servidor"}

    tiempos_cliente = captura_tiempo(msg_cliente)
    tiempos_servidor = captura_tiempo(msg_servidor)

    promedio_cliente = sum(tiempos_cliente) / len(tiempos_cliente)
    promedio_servidor = sum(tiempos_servidor) / len(tiempos_servidor)

    print(f"Tiempo de cliente: {promedio_cliente}, tiempo de servidor: {promedio_servidor}, ratio: {promedio_servidor / promedio_cliente}")

    

