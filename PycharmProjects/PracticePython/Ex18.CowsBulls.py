import random


def rannum():
    return random.randint(1000, 9999)

def cow():
    play = rannum()


    playset = list(str(play))

    guess = 0
    while play != guess:
        guess = input("Introduce un numero: ")
        if(len(guess)>4 or len(guess)<4):
            continue
        else:
            bulls, cows = 0,0
            playguess = list(str(guess))
            for num in range(0,len(playguess)):
                    if playset[num] == playguess[num]: #Si coinciden los indices, el usuario ha acertado un digito del numero
                        cows += 1 #Cows++, hemos encontrado un digito
                    elif playguess[num] in playset: #Sin embargo, puede que no haya acertado el indice pero si el digito
                        bulls += 1 #Bulls++, hemos acertado un digito incorrectamente posicionado







            print("Guess: {0} - COWS = {1} BULLS = {2}".format(guess,cows,bulls))
            if(cows==4):
                print("Contratulations!")
                break









if __name__ == '__main__':
    cow()