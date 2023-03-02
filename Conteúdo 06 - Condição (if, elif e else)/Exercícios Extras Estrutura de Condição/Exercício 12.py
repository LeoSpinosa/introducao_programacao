#Exercício 12
#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
#e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
#O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações.

valorhora = float(input("Informe o valor da sua hora trabalhada: "))
qtdhoras = int(input("Informe a quantidade de horas trabalhadas: "))

salario = valorhora * qtdhoras
sindicato = salario * 0.03
fgts = salario * 0.11


if salario <= 900:
   ir = 0
elif salario <= 1500:
    ir = salario * 0.05
elif salario <= 2500:
    ir = salario * 0.1
else:
    ir = salario * 0.2


print("Salário bruto: ", salario)
print("(-) Imposto de renda: ", ir)
print("(3%) Sindicato: ", sindicato)
print("(11%) FGTS: ", fgts)
print("Total de descontos: ", ir + sindicato)
print("Salário líquido: ", (salario - ir) - sindicato)