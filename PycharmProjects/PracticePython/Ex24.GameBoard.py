import random
name = []
def gameboard(size):
    for num in range(size):
        name.append([0]*size)



def display_board():
    print("x\\y __1__  __2__  __3__  ")
    i = 0
    for num in name:
        i += 1
        print("{0}  ".format(i), end="")
        for elem in num:
                if(elem == 1):
                    print("|__O__|", end="")
                if(elem == 0):
                    print("|_   _|", end="")
                if(elem == -1):
                    print("|__X__|", end="")

        print("")
    print("  "+ "\\_____/" * len(name) + "")


def winner():
    # Filas
    row = []
    for x in range(len(name)):
        elem1 = 0
        for elem in name[x]:
            elem1 += elem
        row.append(elem1)

    #Columnas
    colum = []
    for x in range(len(name)):
        col = 0
        for y in range(len(name)):
            col += name[y][x]

        colum.append(col)
    diag = 0
    for x in range(len(name)):
        diag += name[x][x]
    invdiag = 0
    for x in range(len(name)):
        invdiag += name[x][len(name)-1-x]

    if row.count(3)==1 or colum.count(3)==1 or diag == 3 or invdiag == 3:

        return 1
    elif row.count(-3)==1 or colum.count(-3)==1 or diag == -3 or invdiag == -3:

        return -1
    return 0



def ai_move():
    ran_x = random.randint(0, 2)
    ran_y = random.randint(0, 2)
    if name[ran_x][ran_y] == 0:
        name[ran_x][ran_y] = -1
    else:
        ai_move()





def game():
    gameboard(3)
    while(True):

        '''
            
            name[0] = [0, 1, 1]
            name[1] = [-1, -1, -1]
            name[2] = [1, 0, 1]
        '''

        display_board()
        x,y = (input("Introduce coordenada x y\n >> ").split())


        if(name[int(x)-1][int(y)-1] == -1):
            continue
        else:
            name[int(x)-1][int(y)-1] = 1
        ai_move()
        if winner()==1:
            print("Jugador ha ganado!")
            break
        elif winner()==-1:
            print("CPU ha ganado!")
            break




game()





