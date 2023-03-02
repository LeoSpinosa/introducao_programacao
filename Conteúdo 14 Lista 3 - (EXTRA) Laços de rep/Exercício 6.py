#Exercício 6
#Faça um algoritmo que leia tantos números quanto o usuário desejar e imprima a soma deles.

soma = 0

while True:
    num = int(input("Informe um número: "))
    soma += num
    
    print(f"A soma dos números digitados até então é de: {soma}")