#Exercício 1
#O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.
#Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

#Função:

#●Cálculo do valor a ser pago.

prato = float(input("Informe o peso do prato: "))

def calculopeso (pesoprato):
    pesoprato = prato * 12
    return pesoprato

pesoprato = calculopeso(prato)


print(f"O valor a ser cobrado será de R${pesoprato}")

