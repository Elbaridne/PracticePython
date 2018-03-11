a = [1, 5, 10, 15, 20, 25, 90, 18, 1909]


def primeroyultimo(a):
    c = []
    if(len(a) <= 1):
        print("Tiene uno o cero valores")
    else:
        c.append(a[0])
        c.append(a[-1])
        return c

print(primeroyultimo(a))