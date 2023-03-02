#Exercício 3
#Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

num = 0

for n in range (1,501):
    if n % 2 != 0:
        
        if n % 3 == 0:
            num += n

print(f"A soma dos números ímpares que são múltiplos de 3 de 1 a 500 é de: {num}")