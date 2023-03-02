#Exercício 8
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Informe o preço do primeiro produto: "))
preco2 = float(input("Informe o preço do segundo produto: "))
preco3 = float(input("Informe o preço do terceiro produto: "))

if preco2 > preco1 < preco3:
    print("Compre o produto 1")
elif preco1 > preco2 < preco3:
    print("Compre o produto 2")
else:
    print("Compre o produto 3")