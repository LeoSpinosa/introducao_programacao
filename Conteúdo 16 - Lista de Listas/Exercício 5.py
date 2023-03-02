#Exercício 5
#Crie uma lista com números de 2 à 10 para representar as cartas numéricas de um baralho.
#Multiplique a lista por 4, de forma a ter 4 cartas por número para representar os 4 naipes. Embaralhe as cartas.
#Exercício 5
#Crie uma lista com números de 2 à 10 para representar as cartas numéricas de um baralho.
#Multiplique a lista por 4, de forma a ter 4 cartas por número para representar os 4 naipes. Embaralhe as cartas.

from random import shuffle

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4

shuffle(lista)

print(lista)

#--------------------------------------------

from random import shuffle

cartas = list(range(2,11))
cartas *= 4
print(f"As cartas numéricas do baralho: ")

shuffle(cartas)
print(cartas)
