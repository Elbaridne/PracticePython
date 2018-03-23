import random
import time
print("Piensa en un valor entre 1 y 100")
time.sleep(1)
ran = random.randint(-5,5)
startran = 50 + ran
opt = ('>','<','=')
guess = [i for i in range(1,101)]

def game(arr):
    numg = arr[int(len(arr)/2)-1]
    print("Es el valor mayor, menor o igual que... " + str(numg))
    print(arr)
    inp = input("<, >, =    ")
    if(inp not in opt):
        print("Mal input")
    else:
        if(inp == '>'):
            ng = arr[numg:]
            game(ng)
        if(inp == '<'):
            ng = arr[:numg]
            game(ng)
        if(inp == '='):
            print("We got it!")


game(guess)