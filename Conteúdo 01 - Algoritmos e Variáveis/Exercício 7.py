#Exercício 7
#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.

mes = int(input("Informe o mês: "))
dia = int(input("informe o dia: "))

print("Já se passaram", (mes - 1) * 30 + dia, "dias")
