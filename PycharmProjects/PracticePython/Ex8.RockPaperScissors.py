import random

opt = ['r','p','s']
def rps():
    p1 = input("Jugador 1: ")
    p2 = opt[random.randint(0,2)]
    try:
        opt.index(p1)
        opt.index(p2)
        print("Jugador 2 (CPU): {0}".format(p2))
    except ValueError:
        print("¡Que posicion es esa!")

    if p1 == p2:
        print("Empate")
    else:

        if (p1 == 'r' and p2 == 'p'):
            print("P2 Wins")
        if (p1 == 'r' and p2 == 's'):
            print("P1 Wins")
        if (p1 == 's' and p2 == 'p'):
            print("P1 Wins")
        if (p1 == 's' and p2 == 'r'):
            print("P2 Wins")
        if (p1 == 'p' and p2 == 's'):
            print("P2 Wins")
        if( p1 == 'p' and p2 == 'r'):
            print("P1 Wins")

while(input("¿Jugamos al Rock Paper Scissors? [s] || [n]") == 's'):
    print("Rock (r), Paper (p), Scissors (s)")
    rps()