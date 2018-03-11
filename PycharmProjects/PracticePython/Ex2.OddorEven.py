number = int(input("Introduce un número: "))
if (number % 2) == 1:
    print("Impar")
else :
    print("Par")

    if (number % 4) == 0:
        print("Múltiplo de 4!!!!")



print("Extra: Introduce dos números")
enum = int(input("Primer número: "))
enum2 = int(input("Segundo número: "))
print("{0} / {1} resulta en : {2}".format(enum,enum2,enum/enum2))
