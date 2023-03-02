#Exercício 1
#Desenvolver um algoritmo que leia a altura de 15 pessoas.
#Este programa deverá calcular e mostrar :

#a) A menor altura do grupo;
#b) A maior altura do grupo.

menor_altura = 0
maior_altura = 0

aux = 0
while aux < 5:
    altura = float(input('Digite a sua altura: '))
    if aux == 0:
        menor_altura = altura
        maior_altura = altura
    else:
        if altura < menor_altura:
            altura = menor_altura
        if altura > maior_altura:
            maior_altura = altura
    aux += 1
print(maior_altura)
print(menor_altura)