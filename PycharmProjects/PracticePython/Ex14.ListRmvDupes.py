#1. Usando un loop

a = [1,2,1,3,4,5,2,4]
c = []
for elem in a:
    if elem not in c:
        c.append(elem)
print(c)

d = set()
e = set()
for elem in range(1,10):
    e.add(elem)

for elem in a:
    d.add(elem)

print(d)

# Subconjuntos y Conjuntos
print(e.issuperset(d))
print(e.issubset(d))
print(e.issubset(e))