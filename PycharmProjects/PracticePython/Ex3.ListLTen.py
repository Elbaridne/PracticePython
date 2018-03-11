a = [10, 22, 4, 19, 2, 49, 1, 20, 90, 5, 2, 4]
b = 0
c = []
for i in a:
    b = b+1
    if i <= 5:
        print("Índice {0}: {1} ".format(b,i))
        c.append(i)
print(c)