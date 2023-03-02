#Exercício 3
#Escrev um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado.
#Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

valor = int(input("Informe o número para saber sua fatorial: "))

for n in range (valor - 1,0,-1):
    valor *=  n
print(valor)
