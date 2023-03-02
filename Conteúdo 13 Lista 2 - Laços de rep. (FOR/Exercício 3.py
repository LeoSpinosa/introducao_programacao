#Exercício 3
#Faça um algoritmo que leia 10 números inteiros e calcule o somatório dos números negativos.

negativos = 0

for n in range (0, 2):
    num = int(input("informe um número inteiro: "))
    if num < 0:
        negativos += num
    
print(f"A soma dos número negativos digitados é de {negativos}.")