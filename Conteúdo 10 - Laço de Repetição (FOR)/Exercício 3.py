#Exercício 3
#Somar os números múltiplo de 3, que estão na faixa de 1 à 500.

multiplo = 0

for n in range(1,501):
    if n % 3 == 0:
        multiplo += n

print(f"A soma dos múltiplos de 3 de 1 a 500 é de {multiplo}")