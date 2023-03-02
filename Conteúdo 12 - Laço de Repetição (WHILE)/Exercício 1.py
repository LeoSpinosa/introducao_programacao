#Exercício 1
#Somar os números pares de 1 à 500.

vlr = 1
soma = 0

while vlr <= 501:
    if vlr % 2 == 0:

        soma += vlr
    vlr += 1

print(f"A soma dos pares é de: {soma}")