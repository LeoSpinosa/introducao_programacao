#Exercício 1
#Somar os números pares de 1 à 500.

soma = 0

for n in range (0,501,2):
    if n % 2 == 0:
        soma += n
    
print(soma)