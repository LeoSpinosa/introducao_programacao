#Exercício 1 
#Escreva um programa que solicite:

#1.Tamanho da Lista;
#2.Um valor numérico para cada posição da lista.

#A saída para o usuário deve ser a lista invertida.


lista = []
tamlista = int(input("Quantos itens você deseja armazenar: "))

for n in range (0,tamlista):
    valor = int(input("Informe um valor inteiro para ser armazenado na lista: "))
    lista.append(valor)

lista.reverse()

print(lista)