#Exercício 5
#Faça um algoritmo que leia vários números e informe quantos desses números entre 100 e 200 foramdigitados.
#Quando o valor 0 (zero) for lido o algoritmo deverá cessar sua execução.

vlr = int(input("Quantos números devem ser lidos: "))
contador = 0

for n in range (0,vlr):
    num = int(input("Informe quais números devem ser lidos: "))
    if 100 <= num <= 200:
        contador += 1
    elif num == 0:
        break

print(f"Foram digitados {contador} números entre 100 e 200.")