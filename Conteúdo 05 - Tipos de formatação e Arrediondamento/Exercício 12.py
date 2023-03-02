#Exercício 12
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Informe o valor de um produto: "))
desconto = preco * 0.05

precofinal = preco - desconto
print("Preço com desconto: ", precofinal)