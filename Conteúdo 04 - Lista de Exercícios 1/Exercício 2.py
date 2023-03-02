#Exercício 2 
#Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá.
#Faça um algoritmo para calcular quantos litros de água e de suco são necessários
#para se fazer X litros de refresco(informados pelo usuário).

litrorefresco = float(input("Quantos litros de refresco vão ser feito: "))

agua = litrorefresco * 0.8
suco = litrorefresco * 0.2

print("De água serão necessários ", agua, "litros de água")
print("De suco serão necessários ", suco, "litros")