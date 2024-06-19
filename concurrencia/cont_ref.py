import sys


def dup(a):
    print(f"Cuenta de referencias antes de asignacion: {sys.getrefcount(a)}")
    b = a
    print(f"Cuenta de referencias despues de asignacion: {sys.getrefcount(a)}")

    return b * 2


if __name__ == "__main__":
    a = 6790

    print(f"Cuenta de referencias antes de llamar a la funcion: {sys.getrefcount(a)}")
    c = dup(a)
    print(f"Cuenta de referencias despues de llamar a la funcion: {sys.getrefcount(a)}")
