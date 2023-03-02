#Exercício 1
#Crie um programa que verifique quem pode ir no toboágua do parque aquático.
#1.Solicite a idade.
#2.Solicite a altura.
#3.Solicite o peso.
#4.Só pode brincar quem tiver:

#a) Mais de 12 anos.
#b) No minimo 1,50 de altura
#c) E pesar entre 50kg e 120kg

idade = int(input("Informe a sua idade: "))
altura = float(input("Informe a sua altura: "))
peso = float(input("Informe o seu peso: "))

if idade > 12 and altura >= 1.50 and 120 >= peso >= 50 :
    print("Pode brincar")
else:
    print("Não é permitido brincar")