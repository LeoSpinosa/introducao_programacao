#Exercício 7
#Construa um algoritmo que leia uma quantidade indeterminada de números inteiros positivos e identifique qual foi o maior número digitado.
#O final da série de números digitada deve ser indicado pela entrada de –1.

num = 0
n = 0
maior = 0

while num != -1:
    n += 1
    for n in range(True):
        if n == 1:
            maior == num

    num = int(input("informe um valor: "))
    
    if num > maior:
        maior = num

print(f"O maior número digitado foi: {maior}.")