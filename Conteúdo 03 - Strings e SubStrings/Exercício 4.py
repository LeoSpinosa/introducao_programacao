#Exercício 4
#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.
#Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário.
#Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

horanormal = float(input("Informe quantas horas você trabalhou: "))
horaextra = float(input("Informe quantas horas extras você trabalhou: "))

salariobruto = (horanormal * 10) + (horaextra * 15)
salarioliquido = salariobruto - (salariobruto * 0.1)

print("Seu salário bruto é de: ", salariobruto)
print("Seu salário líquido é de: ", salarioliquido)