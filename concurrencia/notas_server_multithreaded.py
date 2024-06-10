import json
import socket
from threading import Thread

SOCKET_BUFFER = 1024


def extrae_fila(codigo: str) -> list[str]:
    """
    Extrae las notas del archivo notas_arqui.csv del codigo referenciado en formato de lista de strings
    :@param codigo: str que contiene el codigo del alumno a buscar
    :@return: lista de strings conteniendo las notas del codigo referenciado
    """
    with open("notas_arqui.csv", "r") as f:
        contenido = f.read()

    contenido = contenido.split("\n")

    for fila in contenido:
        if codigo in fila:
            notas = fila.split(",")
            print(f"[*] Retornando: {notas}")
            return notas
    
    return list()


def procesa_requerimiento(notas: list[str], modo: str) -> dict:
    """
    Procesa el requerimiento del cliente a partir de las notas recuperadas. Si el modo es "servidor",
    calcula la nota en esta funcion y retorna el valor de nota final. Si el modo es "cliente", retorna todas las notas parciales
    en el diccionario, con sus llaves correspondientes. Siempre retorna con una llave de estado.
    :@param notas: lista de strings conteniendo las notas a procesar.
    :@param codigo: Codigo del alumno sobre el cual se van a procesar las notas.
    :@param modo: Modo de operación, puede ser 'cliente' o 'servidor'.
    :@return: diccionario conteniendo el resultado del requerimiento.
    """
    match modo:
        case "cliente":
            d = dict()
            d["estado"] = "exito"
            for idx in range(14):
                d[f"lab{idx + 1}"] = int(notas[idx + 1])
            d["e1"] = notas[15]
            d["e2"] = notas[16]
        case "servidor":
            notas_lab = 0
            for idx in range(14):
                notas_lab += int(notas[idx + 1])
            notas_lab /= 14

            e1 = int(notas[15])
            e2 = int(notas[16])

            nota = (notas_lab * 0.5) + (e1 * 0.25) + (e2 * 0.25)

            d = {"estado": "exito", "nota": nota}
        case _:
            d = {"estado": "error", "mensaje": "Valor para modo no valido"}

    return d


def procesa_dato(dato: bytes) -> dict:
    """
    Convierte stream de bytes en un diccionario y trata de procesar el requerimiento
    :@param dato: cadena de bytes que contiene el requerimiento
    :return: diccionario con el resultado del procesamiento del requerimiento
    """
    try:
        msg_cliente = json.loads(dato)
        if "codigo" in msg_cliente.keys() and "modo" in msg_cliente.keys():
            notas = extrae_fila(msg_cliente["codigo"])
            if len(notas) > 0:
                msg_respuesta = procesa_requerimiento(notas, msg_cliente["modo"])
            else:
                msg_respuesta = {"estado": "error", "mensaje": "codigo no contiene notas registradas"}
        else:
            msg_respuesta = {"estado": "error", "mensaje": "Formato de JSON incorrecto"}                
    except json.decoder.JSONDecodeError:
        msg_respuesta = {"estado": "error", "mensaje": "No se pudo decodificar el mensaje en JSON"}            

    return msg_respuesta


def handle_client(conn: socket.socket, client_address):
    """
    Funcion para manejar la operacion de un cliente individual conectado al servidor
    :@param conn: Objeto de socket para realizar la comunicacion con el servidor
    :@param client_address: Datos de conexion del cliente
    :return: None
    """
    print(f"[*] Conexion establecida con {client_address[0]}:{client_address[1]}")

    try:
        while True:
            dato = conn.recv(SOCKET_BUFFER)
            if dato:
                msg_respuesta = procesa_dato(dato)
                msg_respuesta_str = json.dumps(msg_respuesta)
                conn.sendall(msg_respuesta_str.encode("utf-8"))
            else:
                print("[*] No hay mas datos de parte del cliente")
    except ConnectionResetError:
        print("[!] Cliente cerro la conexion de manera abrupta")
    finally:
        print("[*] Cerrando la conexion")
        conn.close()


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"[*] Levantando servidor en direccion {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)
    sock.listen(5)

    while True:
        print(f"[*] Esperando conexiones...")
        conn, client_address = sock.accept()

        t = Thread(target=handle_client, args=(conn, client_address))
        t.start()
