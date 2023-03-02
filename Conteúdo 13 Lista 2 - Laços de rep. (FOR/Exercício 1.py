#Exercício 1
#Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir.
#Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.

vlr = int(input("Quantos números devem ser lidos: "))

for n in range (0, vlr):
    num = int(input("Informe quais os números: "))
    for a in range (num - 1, 0, -1):
        num *= a
    print(f"A fatorial desse número é {num}.")

