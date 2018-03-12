frase = input("Introduce una frase con espacios en blanco: ")

fseparada = frase.split()

fsepfirst = fseparada[0]
fseparada[0] = fseparada[-1]
fseparada[-1] = fsepfirst

nuevafrase = "__SKR__".join(fseparada)
print(nuevafrase)