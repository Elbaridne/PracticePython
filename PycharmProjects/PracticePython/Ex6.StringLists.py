palindrome = input("Introduce una frase: ")
copypalin = palindrome[::-1]
if(copypalin == palindrome):
    print("Tenemos un palindromo")
else:
    print("Parece que no es palíndromo")

