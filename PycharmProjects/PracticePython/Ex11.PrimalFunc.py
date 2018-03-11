def divisores(num):
    c = []
    for i in range(num):
        if (i == 0):
            continue
        if (num % i) == 0:
            c.append(i)
    c.append(num)
    return c


def primo(divisor):
    if len(divisor) == 2:
        print("Es un numero primo")
    else :
        print("No es primo")

if __name__ == '__main__':
    num = input("Introduce el numero: ")
    primo(divisores(num))
