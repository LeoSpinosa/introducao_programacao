#Exercício 9
#João recebeu seu salário de R$1200,00 e precisa pagar duas contas (C1=R$200,00eC2=R$120,00)
#que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
#Faça um algoritmo que calcule e mostre quanto restará do salário do João.

salario = 1200

conta1 = 200 + 200 * 0.02
conta2 = 120 + 120 * 0.02

salariofinal = (salario - conta1) - conta2

print("Restou do salário um total de: ", salariofinal)