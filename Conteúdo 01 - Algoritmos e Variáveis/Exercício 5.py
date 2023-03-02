#Exercício 5
#Escreva um algoritmo para ler o nome e a idade de uma pessoa e exibir quantos dias de vida ela possui.
#Considere sempre anos completos, e que um ano possui 365 dias.
#Ex: uma pessoa com 19 anos possui 6935 dias de vida;
#veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935 DIAS.

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

vida = idade * 365

print("Parabéns", nome, "você ja viveu", vida, "dias.")