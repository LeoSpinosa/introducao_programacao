#Exercício 6
#Solicite que o usuário insira seu nome completo e informe quantos caracteres ele possui.

nome = input("Informe seu nome completo: ")

char = 0

for n in (nome):
    char += 1
print(f"Seu nome possui {char} caracteres.")