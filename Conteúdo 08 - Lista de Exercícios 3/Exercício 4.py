#Exercício 4
#As maçãs custam R$1,30 cada se forem compradas menos de uma dúzia, e R$1,00se forem compradas pelo menos 12.
#Escreva um programa que leia o número demaçãs compradas, calcule e escreva o custo total da compra.

qtdmaça = int(input("Informe quantas maças foram compradas: "))

if qtdmaça < 12:
    print("Toral a pagar: ", qtdmaça * 1.3, "reais")

else:
    print("Total a pagar: ", qtdmaça, "reais")