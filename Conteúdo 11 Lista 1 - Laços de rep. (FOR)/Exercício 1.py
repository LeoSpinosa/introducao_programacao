#Exercício 1
#Desenvolver um algoritmo que leia a altura de 15 pessoas.
#Este programa deverá calcular e mostrar :

#a) A menor altura do grupo;
#b) A maior altura do grupo.

altMaior = 0
altMenor = 0

for n in range (1,16):

    altura = float(input("Informe sua altura: "))

    if n == 1:

        altMenor = altura

        altMaior = altura 

    if altura > altMaior:

        altMaior = altura

    elif altura < altMenor:

        altMenor = altura



print (f"A MAIOR altura é de {altMaior}")

print (f"A MENOR altura é de {altMenor}")

