#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual:

#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Informe o seu salário atual: "))


reajuste1 = 0.2
reajuste2 = 0.15
reajuste3 = 0.1
reajuste4 = 0.05



if 0 <= salario <= 280:
    salarioaumento = (salario + (salario * reajuste1))
elif 280 < salario <= 700:
   salarioaumento = (salario + (salario * reajuste2))
elif 700 < salario <= 1500:
    salarioaumento = (salario + (salario * reajuste3))
else:
    salarioaumento = (salario + (salario * reajuste4))



if 0 <= salario <= 280:
    rajuste = reajuste1
elif 280 < salario <= 700:
   reajuste = reajuste2
elif 700 < salario <= 1500:
    reajuste = reajuste3
else:
    reajuste = reajuste4

print("Salário antes do reajuste: ", salario)
print("Reajuste salárial: ", reajuste * 100, "%")
print("Valor do aumento: ", salarioaumento - salario)
print("Novo salário: ", salarioaumento)
