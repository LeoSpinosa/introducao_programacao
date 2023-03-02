#Exercício 4
#Escreva um programa que solicite:

#1) Tamanho da Lista.
#2) Um valor numérico para cada posição da lista.

#Percorra a lista para substituir todos valores negativos por Zero.

lista = []

tamanho = int(input("\nInforme o tamanho da lista que você deseja: "))
print("\n")
for n in range(1, tamanho +1):
    vlr = int(input("Informe um valor a ser adicionado na lista: "))
    lista.append(vlr)

for a in range(0, len(lista)):
    if lista[a] < 0:
        lista[a] = 0
         

print(lista)






    