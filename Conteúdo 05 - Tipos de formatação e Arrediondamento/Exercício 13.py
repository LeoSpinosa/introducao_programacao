#Exercício 13
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o seu salário: "))
aumento = salario * 0.15
salariofinal = salario + aumento

print("Salário final com aumento: ", salariofinal)