with open("primenumbers.txt",'r') as f:
    prime = [int(i) for i in f]
    
with open("happynumbers.txt", 'r') as f:
    happy = [int(i) for i in f]

def diff(ar1,ar2):
    set1,set2= set(ar1), set(ar2)
    return set1.intersection(set2)

print(diff(prime,happy))