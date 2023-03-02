#Exercício 6
#Faça um algoritmo que receba o valor do salário mínimo e o valor do salário de um funcionário
#calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

salariominimo = int(input("Informe o valor do salário mínimo: "))
salariofuncionario = int(input("Informe o valor do seu salário: "))

salariototal = salariofuncionario / salariominimo

print("Você ganha", salariototal, "de salários mínimos")