import random

list_ran = random.sample(range(1000),100)
list_ran.sort()
print(list_ran)
num = int(input("Elemento a buscar binariamente"))

def elesearch(list):
    if(int(input("Elemento a buscar: ")) in list_ran):
        print(True)
    else:
        print(False)

def binarysearch(list, num):
    half_len_list = int(len(list)/2)
    if(num == list[half_len_list]):
        return True
    elif(half_len_list == 1):
        return False
    elif(num > list[half_len_list]):
        newl = list[half_len_list:]
        return binarysearch(newl,num)
    else:
        newl = list[:half_len_list]
        return binarysearch(newl,num)

print(binarysearch(list_ran,num))