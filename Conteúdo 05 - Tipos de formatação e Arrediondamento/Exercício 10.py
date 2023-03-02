#Exercício 10
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Quantos reais você tem: "))
dolar = 3.27

conevrsao = reais / dolar

frase1 = "Com essa quantidade de reais é possível comprar %.2f"%(conevrsao)
print(frase1)