#Exercício 4
#Faça um programa que simule um lançamento de dados.
#Lance o dado 100 vezes e armazene os resultados em um vetor.
#Depois, mostre quantas vezes cada valor foi conseguido.
#Dica: use um vetor de contadores (1 - 6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.

from random import choice

lado1 = 0
lado2 = 0
lado3 = 0
lado4 = 0
lado5 = 0
lado6 = 0

dado = [1, 2, 3, 4, 5, 6]

for n in range (1, 101):

    landado = choice(dado)

    if landado == 1:
        lado1 += 1
    elif landado == 2:
        lado2 += 1
    elif landado == 3:
        lado3 += 1
    elif landado == 4:
        lado4 += 1
    elif landado == 5:
        lado5 += 1
    else:
        lado6 += 1

print(f'''1 foi tirado {lado1} vezes.
2 foi tirado {lado2} vezes
3 foi tirado {lado3} vezes
4 foi tirado {lado4} vezes
5 foi tirado {lado5} vezes
6 foi tirado {lado6} vezes''')


#------------------------------------------------------

from random import randint

vetorcontador = [0, 0, 0, 0, 0, 0]

for n in range (1, 100):
    
    dado = randint(1,6)

    if dado == 1:
        vetorcontador[0] += 1
    elif dado == 2:
        vetorcontador[1] += 1
    elif dado == 3:
        vetorcontador[2] += 1
    elif dado == 4:
        vetorcontador[3] += 1
    elif dado == 5:
        vetorcontador[4] += 1
    elif dado == 6:
        vetorcontador[5] += 1

print(f'''1 foi tirado {vetorcontador[0]} vezes.
2 foi tirado {vetorcontador[1]} vezes
3 foi tirado {vetorcontador[2]} vezes
4 foi tirado {vetorcontador[3]} vezes
5 foi tirado {vetorcontador[4]} vezes
6 foi tirado {vetorcontador[5]} vezes''')  

