def fibonacci(numero, recursion):
    if recursion == 0:
        print("Final")
        return 0
    else:
        return [numero, fibonacci(numero + numero, recursion=recursion-1)]

print(fibonacci(1,10))