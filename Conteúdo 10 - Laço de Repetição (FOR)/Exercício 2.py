#Exercício 2
#Somar os números ímpares de 1 à 500.

soma = 0

for n in range (1,501,2):
    if n % 2 != 0:
        soma += n
    
print(soma)