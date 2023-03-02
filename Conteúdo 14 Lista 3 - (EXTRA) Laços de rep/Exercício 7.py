#Exercício 7
#Faça um algoritmo que permita ao usuário informar a idade de quantas pessoas ele desejar.
#Após isso o algoritmo deve informar a soma das pessoas maiores de idade e a média de idade das pessoas maiores de idade informadas.

pessoas = int(input("Quantas pessoas você deseja informar: "))
maior = 0
total = 0

for n in range (0, pessoas ):
    idade = int(input("Informe a idade das pessoas: "))

    if idade > 18:
        maior += 1
        total += idade

print(f"O total de pessoas maiores de idade é de: {maior} pessoas")
print(f"A média de idade das pessoas maiores de idade é de {total / maior} anos")

