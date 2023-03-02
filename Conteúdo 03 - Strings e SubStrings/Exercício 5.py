#Exercício 5
#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos:
#Lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros.
#Se um comerciante compra uma determinada  quantidade  de  cada  formato faça  um  algoritmo  para  calcular quantos litros de refrigerante ele comprou.

lata350 = int(input("informe a quantidade de latas de 350ml compradas: "))
garrafa600 = int(input("informe a quantidade de garrafas de 600ml compradas: "))
garrafa2l = int(input("Informe a quntidade de garrafas de 2L compradas: "))

qtdlata350 = lata350 * 0.35
qtdgarrafa600 = garrafa600 * 0.6
qtdgarrafa2l = garrafa2l * 2

totallitros = qtdlata350 + qtdgarrafa600 + qtdgarrafa2l

print("Foram comprados um total de", totallitros, "litros de refrigerante.")