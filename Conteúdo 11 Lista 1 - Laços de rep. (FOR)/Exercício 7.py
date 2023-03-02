#Exercício 7
#Solicite que o usuário insira seu nome completo e apresente apenas o primeiro nome:

#a) Na vertical;
#b) Na horizontal.

nome = input("Informe seu nome completo: ")
horizontal = ""

for letra in (nome):
    if letra == " ":
        print(horizontal)
        break
    print(letra)
    
    horizontal += letra