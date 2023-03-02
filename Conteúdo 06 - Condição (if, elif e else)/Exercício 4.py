#Exercício 4
#Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano.
#Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo.
#Mostre uma mensagem informando o saldo médio e o valor do crédito.

#Saldo médio           Percentual
# de 0 a 200         nenhum crédito
#de 201 a 400       20% do valor do saldo médio
#de 401 a 600       30% do valor do saldo médio
#acima de 601       40% do valor do saldo médio

saldo = float(input("Informe o seu saldo: "))

saldomedio = saldo / 12


if 0 <= saldomedio <= 200:
    credito = "Nenhum crédito"
elif 201 <= saldomedio <= 400:
    credito = saldomedio * 0.2
elif 401<= saldomedio <= 600:
    credito = saldomedio * 0.3
else:
    credito = saldomedio * 0.4

print("Seu saldo médio é de %.2f e o valor do crédito será de %.14s"%(saldomedio, credito))