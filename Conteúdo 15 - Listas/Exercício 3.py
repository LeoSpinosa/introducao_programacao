#Exercício 3
#Desenvolver um algoritmo que leia a altura de pessoas e armazene em uma lista, até que o 0 (zero) seja informado.
#Este programa deverá calcular e mostrar :

#a) A menor altura do grupo;
#b) A maior altura do grupo.

lista = []

while True:
    alt = float(input("Informe a altura de uma pessoa (0 para encerrar o progama): "))
    lista.append(alt)

    if alt == 0:
        break
    
    maior = lista[0]
    menor = lista[0]

    for a in lista:

        if a > maior:
            maior = a
        elif a < menor:
            menor = a
        

print(f"A maior altura informada foi {maior} e a menor foi {menor}.")
    


        
