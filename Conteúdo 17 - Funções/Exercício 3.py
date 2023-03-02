#Exercício 3
#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%. Após o aumento, desconte 8% de impostos.
#mprima o salário inicial, o salário com o aumento e o salário final.

#Funções:

#● Calcular aumento.
#● Calcular desconto.
#● Calcular o salário final.

salario = float(input("Informe o seu salário: "))

def calculoaumento(aumento):
    aumento = (salario * 0.15) + salario
    return aumento

aumento = calculoaumento(salario)
    
def calculoimposto(imposto):
    imposto = aumento - (aumento * 0.08)
    return imposto

imposto = calculoimposto(aumento)

print(f"O salário inicial era de R${salario}")
print(f"O salário com aumento é de R${aumento}")
print(f"O salário com aumento e descontos de impostos é de R${imposto}")