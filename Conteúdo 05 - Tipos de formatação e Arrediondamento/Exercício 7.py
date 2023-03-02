#Exercício 7 
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2) / 2

frase1 = ("Baseado em suas notas, sua média é de {}").format(media)
print(frase1)