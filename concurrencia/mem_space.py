import time
from threading import Thread

var_global = 0


def inc():
    global var_global

    print("iniciando funcion de incremento")
    var_global += 1
    time.sleep(0.5)
    print("Saliendo de funcion de incremento")


if __name__ == '__main__':
    print(f"El valor inicial de variable global es {var_global}")
    threads = list()

    for _ in range(3):
        t = Thread(target=inc)
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

    print(f"El valor final de variable global es {var_global}")


