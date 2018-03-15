import random
lista = random.sample(range(100),10)

print(lista)

def quicksort(lista):
    pivot = lista[len(lista)-1]
    izq = 0
    der = len(lista)-2
    while(True):
        while(lista[izq]<pivot):

            izq = izq + 1
            continue

        while(lista[der]>pivot and der > 0):

            der = der - 1
            continue



        if(izq >= der):
            break

        else:

            aux1 = lista[der]
            aux2 = lista[izq]
            lista[izq] = aux1
            lista[der] = aux2
            continue

    aux1= lista[izq]
    lista[izq]=pivot
    lista[len(lista)-1]=aux1
    listaizq = lista[0:lista.index(pivot)]
    listader = lista[lista.index(pivot):]
    print("Lista izq: {0}".format(listaizq))
    if len(listaizq) - len(listader) <= 0:
        return []
    else :
        print("{0}{1}".format(listaizq,listader))
        a = quicksort(listaizq) + quicksort(listader)
        return a




print(lista)
quicksort(lista)
print(lista)