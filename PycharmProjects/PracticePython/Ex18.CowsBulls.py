import random


def rannum():
    return random.randint(0, 9999)

def cow():
    play = rannum()


    playset = list(str(play))
    print(playset)
    guess = 0
    while play != guess:
        guess = input("Introduce un numero: ")
        if(len(guess)>4 or len(guess)<4):
            continue
        else:
            playguess = list(str(guess))

            bulls = 0
            cows = 0
            alreadyguessed = list()
            for guss in playguess:
                if not alreadyguessed.__contains__(guss):
                    alreadyguessed.append(guess)
                else :

                    try:
                        playset.index(guss) == -1
                    except ValueError:
                        continue
                    if playguess.index(guss) == playset.index(guss):
                        cows+= 1

                        continue

            print("Guess: {0} - COWS = {1} BULLS = {2}".format(guess,cows,len(alreadyguessed)))
            if(cows==4):
                print("Contratulations!")
                break









if __name__ == '__main__':
    cow()