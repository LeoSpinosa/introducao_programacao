#Exercício 3
#Crie um algoritmo que leia quatro valores digitados pelo usuário: n, a, b, c. 
#a) Se n = 1 imprimir os três valores a, b, c em ordem crescente.
#b) Se n = 2 escrever os três valores a, b, c em ordem decrescente.
#c) Se n = 3 escrever os três valores a, b, c de forma que o maior fique no meio.


n = int(input("Informe o valor de n (1, 2 ou 3): "))
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))


if n == 1:

    if a <= b <= c:
        crescente = a, b, c
    elif a < c < b:
        crescente = a, c, b
    elif b < a < c:
        crescente = b, a, c
    elif b < c < a:
        crescente = b, c, a
    elif c < a < b:
        crescente = c, a, b
    elif c < b < a:
        crescente = c, b, a

        print(crescente)

elif n == 2:

    if a >= b >= c:
        decrescente = a, b, c
    elif a > c > b:
        decrescente = a, c, b
    elif b > a > c:
        decrescente = b, a, c
    elif b > c > a:
        decrescente = b, c, a
    elif c > a > b:
        decrescente = c, a, b
    elif c > b > a:
        decrescente = c, b, a 

    print(decrescente)

elif n == 3:

    if a <= b >= c:
        maior = a, b, c
    elif a < c > b:
        maior = a, c, b
    elif b < a > c:
        maior = b, a, c
    elif b < c > a:
        maior = b, c, a
    elif c < a > b:
        maior = c, a, b
    elif c < b > a:
        maior = c, b, a 

    print(maior)

else: 

    print("Valor inválido")
