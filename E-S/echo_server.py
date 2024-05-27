import socket

SOCKET_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5500)

    print(f"[*] Levantando servidor en dirección {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("[*] Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexión establecida con {client_address[0]}:{client_address[1]}")    

        try:
            while True:
                dato = conn.recv(SOCKET_BUFFER)

                if dato:
                    print(f"[+] Recibí: {dato}")
                    conn.sendall(dato)
                else:
                    print("[*] No hay más datos de parte del cliente")
                    break
        except ConnectionResetError:
            print("[!] Cliente cerró la conexión abruptamente")
        finally:
            print("[*] Cerrando la conexión")
            conn.close()



