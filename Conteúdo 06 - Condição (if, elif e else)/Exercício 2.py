#Exercício 2
#Faça um algoritmo que leia um número inteiro e mostre:
#● Mensagem indicando se este número é par ou ímpar.
#● Mensagem indicando se este número é positivo ou negativo.

numero = int(input("Informe um número: "))

if (numero % 2) == 0:
    situacao = "Número par"
else:
    situacao = "Número negativo"

print(situacao)

if numero > 0:
    situacao = "Número positivo"
else:
    situacao = "Número negativo"

print(situacao)
