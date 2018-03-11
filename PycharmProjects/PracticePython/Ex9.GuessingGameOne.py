import random
def ranGame():
    tries = 0
    ran = random.randint(1,9)
    while(True):
        tries = tries + 1
        try:
            inp = int(input("Adivina el número (1-9): "))
        except:
            print("No es un Numero (NaN)")
            continue

        if(inp == ran):
            print("Lo has conseguido en {0} intentos!".format(tries))
            if(input("¿Quieres seguir jugando?: [s]:")=='s'):
                ranGame()
            break
        elif(inp > ran):
            print("Mas bajo")
        else:
            print("Más alto")

ranGame()