#Exercício 4
#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
#Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas
#calcule e mostre a comissão e o salário final do funcionário.

salario = int(input("Informe seu salário fixo: "))
vendas = int(input("Informe o valor das suas vendas: "))

comissao = vendas * 0.04
salariofinal = salario + comissao

print("Total de comissão: ", comissao)
print("Total do salário: ", salariofinal)