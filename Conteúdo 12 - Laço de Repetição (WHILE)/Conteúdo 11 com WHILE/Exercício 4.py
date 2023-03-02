#Exercício 4
#Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos.

resultado = 0
comeco = 1
fim = 6

while comeco < fim:
    comeco += 1
    a = int(input("Informe o valor de a: "))
    if a < 0:
        resultado += 1
    

print(f"Foram digitados {resultado} valores negativos.")