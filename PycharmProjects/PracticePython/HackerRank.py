a = 73
c = a % 5
if(c == 3):
    a = a + 2
if(c == 4):
    a = a + 1

print(a)

import sys


def solve(grades):
    for el in grades:
        c = el % 5
        if(c == 3):
            el = el + 2
        if(c == 4):
            el = el + 1
    return el

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
