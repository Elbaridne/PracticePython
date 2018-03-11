import random

a = []
b = []
c = []

for i in range(100):
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))
for i in a:
    for j in b:
        if(i == j):
            if(c.__contains__(i)):
                continue
            c.append(i)
c.sort()
print(c)
