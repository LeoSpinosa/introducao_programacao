#Exercício 3
#Somar os números múltiplo de 3, que estão na faixa de 1 à 500.

vlr = 1
soma = 0

while vlr <= 501:
    if vlr % 3 == 0:

        soma += vlr
    vlr += 1

print(f"A soma dos múltilpos de 3 é de: {soma}")