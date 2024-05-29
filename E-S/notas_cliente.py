import json
import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)

    print(f"[*] Conectando a servidor en {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    # msg = {"codigo": "20240100", "modo": "cliente"}
    msg = {"codigo": "20240100", "modo": "servidor"}
    msg_str = json.dumps(msg)

    print(f"[*] Preparándome para enviar {msg_str}")
    sock.sendall(msg_str.encode("utf-8"))

    data = sock.recv(SOCK_BUFFER)

    print(f"[!] Recibí: {data}")

    print(f"[*] Terminando operación, cerrando el socket")

    sock.close()

