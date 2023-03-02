#Exercício 1
#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos.
#A prefeitura deseja saber: 

#a) Média do salário da população;
#b) Média do número de filhos;
#c) Maior salário;
#d) Percentual de pessoas com salário até R$100,00.

#O final da leitura de dados se dará com a entrada de um salário negativo.

numbHabitantes = 0
somaSalario = 0
qtdFilhos = 0
maiorsalario = 0
menor = 0

while True:

    salario = float(input("Informe seu salario: "))

    if salario > 0:

        somaSalario += salario

        numbHabitantes += 1

        filhos = int(input("Informe a quantidade de filhos: "))

        qtdFilhos += filhos

        if salario > maiorsalario:
            maiorsalario = salario
        
        elif salario < 100:
                menor += 1
                porcento =  menor * 100 / numbHabitantes 

    elif salario < 0:
        print(f"Final da coelta de dados.\n\n")
        break

    

print(f"A média de salário da popução é de {somaSalario / numbHabitantes}")
print(f"A média de filhos da popução é de {qtdFilhos / numbHabitantes}")
print(f"O maior salário da população é de {maiorsalario} reais")
print(f"A porcentagem de pessoas com salário menor de 100 reais é de: {porcento}%")