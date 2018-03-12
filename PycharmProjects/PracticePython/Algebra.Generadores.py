# Generadores de un grupo cíclico de orden (x)
# gen(x) devuelve lista de generadores


def primo(dato, dato2):
    divisores = 0
    for i in range(1, dato2):
        if dato % i == 0 and dato2 % i == 0:
            divisores = divisores + 1

    if divisores == 1:
        return dato


def gen(orden):
    c = []
    for i in range(1, orden):
        if primo(i, orden) is None:
            continue
        else:
            c.append(primo(i,orden))
    return c

print gen(8)

