from _datetime import datetime
date = datetime.now()
year = date.year
nombre = ''
edad = 0

def preguntar() :
    nombre = input("¿Cual es tu nombre?  :  ")
    edad = int(input("Vale, {0}, y tu edad?  : ".format(nombre)))
def calc(nombre, edad) :
    if(edad >= 100) :
        print("Parece que ya has alcanzado tu primer centenario, enhorabuena!")
    else :
        yyears = 100 - edad
        nyears = year + yyears
        print("Segun mis cálculos, {0}, todavía te quedan {1} años par alcanzar los 100.".format(nombre, yyears))
        print("Esto sucedera en el año : {0}".format(nyears))

while(True) :
    preguntar()
    calc(nombre, edad)
    flag = input("Pulsa Enter para continuar el bucle \nCualquier otro carácter y Enter para salir")
    if(flag != '') :
        break
