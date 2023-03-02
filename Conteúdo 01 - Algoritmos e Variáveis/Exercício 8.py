#Exercício 8
#Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%.
#Após o aumento, desconte 8% de impostos.
#Imprima o salário inicial, o salário com o aumento e o salário final.

salario = float(input("Informe o seu salário: "))

aumentosalario = salario * 0.15
imposto =  aumentosalario * 0.08

print("Salário inicial: ", salario)
print("Salario com aumento: ", aumentosalario + salario)
print("Salário final: ", (aumentosalario + salario) - imposto )