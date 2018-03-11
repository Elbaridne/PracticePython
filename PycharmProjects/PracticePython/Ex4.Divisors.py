num = int(input("Introduce un numero para conocer su lista de divisores: "))
for i in range(num) :
    if(i==0) :
        continue
    if(num % i) == 0:
        print("{0} es un divisor de {1}".format(i,num))
print("{0} es obviamente un divisor de {0}".format(num))