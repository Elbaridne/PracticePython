palabras = ["pez","loquito","dieciocho","memoria","lahascagado"]
simbolos = ["!","..","?"]

import random
def construirPassword(a):
    password = ''
    if(a == 2):
        rannum = random.randint(30,400)
        password = str(rannum) + palabras[random.randint(0,4)] + simbolos[random.randint(0,len(simbolos)-1)] + palabras[random.randint(0,len(palabras)-1)].capitalize()
        print(password)
    if(a == 1):
        rannum = random.randint(90,1000)
        password = str(rannum) + palabras[random.randint(0,4)].capitalize() + "!!"
        print(password)
    if(a == 0):
        rannum = random.randint(100,4999)
        password = palabras[random.randint(0,4)].capitalize() + str(rannum)
        print(password)

def main():

    while(True):
        print("Creador de contraseñas, que nivel de seguridad quieres")
        opcion = int(input("[0] Floja, [1] Media, [2] Fuerte, [3] Salir"))
        if(type(opcion)!=int):
            print("No es una opcion...")
        elif(opcion == 3):
            break
        elif(opcion > 3):
            print("No es una opcion...")
        else:
            construirPassword(opcion)


if __name__ == '__main__':
    main()