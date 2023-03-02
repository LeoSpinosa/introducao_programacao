#Exercício 1
#Três amigos, Carlos, André e Felipe. Decidiram rachar igualmente a conta de um bar.
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar. 
#Mas faça com que Carlos e André não paguem centavos.
#Ex: uma conta de R$101,53 resulta em R$33,00 para Carlos
#R$33,00 para André e R$35,53 para Felipe. 

totalconta = float(input("Valor total da conta: "))

partecarlos = totalconta // 3
parteandre = totalconta // 3
partefelipe = (totalconta - partecarlos) - parteandre

print(partecarlos)
print(parteandre)
print(partefelipe)
