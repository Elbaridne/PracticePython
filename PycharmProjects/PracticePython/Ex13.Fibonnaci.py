a = [1, 1, 2, 3, 5, 8, 13]

def fibonacci(numero):
    if numero==1 or numero==0 :
        return numero
    if numero!=0 :
        return fibonacci(numero-1) + fibonacci(numero-2)


for a in range(1,10):
    print("Sucesion Fibonacci {0} : {1}".format(a,fibonacci(a)))

