#Exercício 15
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmpercorridos = float(input("Informe quantos KM foram percorridos: "))
diasalugados = int(input("Informe quantos dias o carro ficou alugado: "))

precodias = diasalugados * 60
precokm = kmpercorridos * 0.15


frase1 = "Será necessário pagar um total de {} somando os KM percorridos e os dias alugados".format(precodias + precokm)
print(frase1)