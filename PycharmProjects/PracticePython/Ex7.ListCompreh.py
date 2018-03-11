a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [a[i] for i in range(len(a)) if i % 2 == 1]
print(b)