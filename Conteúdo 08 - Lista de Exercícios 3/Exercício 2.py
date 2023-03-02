#Exercício 2
#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#1.Álcool:

#a) Até 20 litros, desconto de 3% por litro;
#b) E acima de 20 litros, desconto de 5% por litro;

#2.Gasolina:

#a) Até 20 litros, desconto de 4% por litro;
#b) E acima de 20 litros, desconto de 6% por litro.

#Escreva um algoritmo que leia o número de litros vendidos,
#o tipo de combustível(A-álcool, G-gasolina) e imprima o valor a ser pago pelo cliente.
#Considere que opreço do litro da gasolina é R$ 5,15 e o preço do litro do álcool é R$ 4,29.

litros = float(input("Informe quantos litros foram vendidos: "))
tipo = input("Informe o tipo de gasolina (A para álcool, G para gasolina): ")

gasolina = litros * 5.15
alcool = litros * 4.29

if tipo == "A":

    if litros <= 20:
        desconto = 0.03 * alcool

    elif litros > 20:
        desconto = 0.05 * alcool

    print("Total a ser pago é de: %.2f reais"%(alcool - desconto))


if tipo == "G":

    if litros <= 20:
        desconto = 0.04 * gasolina
    
    else:
        desconto = 0.06 * gasolina

    print("Total a ser pago é de: %.2f reais"% (gasolina - desconto))
