#Exercício 7
#Solicite que o usuário insira seu nome completo e apresente apenas o primeiro nome:

#a) Na vertical;
#b) Na horizontal.

nome = input("Informe seu nome completo: ")
contador = 0

while len(nome) > contador:
    if nome[contador] == " ":
        break
    print(nome[contador])
    contador += 1

print(nome[0:contador])