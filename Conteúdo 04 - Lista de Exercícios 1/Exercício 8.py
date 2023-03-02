#Exercício 8
#Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
#a) a idade dessa pessoa em anos;
#b) a idade dessa pessoa em meses;
#c) a idade dessa pessoa em dias;
#d) a idade dessa pessoa em semanas.

anonascimento = int(input("Informe o ano do seu nascimento: "))
anoatual = int(input("Informe o ano atual: "))

idade = anoatual - anonascimento

idademeses = idade * 12 

idadedias = idademeses * 30

idadesemana = idadedias // 7

print("Sua idade em anos: ", idade)
print("Sua idade em meses: ", idademeses)
print("Sua idade em dias: ", idadedias)
print("Sua idade em semanas: ", idadesemana)