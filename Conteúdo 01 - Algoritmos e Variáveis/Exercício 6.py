#Exercício 6
#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) 
#e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

valorprato = float(input("Informe o peso do prato em KG: "))

total = valorprato * 12

print ("Total a pagar:", total, "reais")