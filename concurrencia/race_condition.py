from concurrent.futures import ThreadPoolExecutor
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
    
    def update(self, nombre):
        print(f"Thread {nombre}: Iniciando actualizacion")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {nombre}: Ha finalizado la actualizacion")


if __name__ == "__main__":
    workers = 2
    tasks = workers

    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for idx in range(tasks):
            executor.submit(db.update, idx)

    print(f"Valor final de la base de datos: {db.value}")
