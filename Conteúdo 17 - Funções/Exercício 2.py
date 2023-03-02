#Exercício 2
#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.
#Função:

#● Calcular a quantidade de dias que se passaram.

dia = int(input("Informe em que dia do mês estamos: "))
mes = int(input("Informe em que mês estamos: "))

def calculotempo (tempo):
    tempo = (mes * 30) + dia
    return tempo

tempo = calculotempo((mes * 30) + dia)


print(f"Ja se passarm {tempo} dias")

