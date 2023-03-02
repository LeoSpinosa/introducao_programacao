#Exercício 2
#Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

comeco = 100
fim = 200

while comeco < fim:
    comeco += 1
    if comeco % 2 != 0:
        
        print(comeco)