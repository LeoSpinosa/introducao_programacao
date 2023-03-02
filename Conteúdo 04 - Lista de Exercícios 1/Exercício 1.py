#Exercício 1
#Pedrinho tem um cofrinho com muitas moedas,e deseja saber quantos reais conseguiu poupar.
#Faça um algoritmo para ler a quantidadede de cada tipo de moeda,
#e imprimir o valor total economizado, em reais.
#Considere que exista mmoedas de 1, 5, 10, 25 e 50 centavos,e ainda moedas de 1 real.
#Não havendo moeda de um tipo, a quantidade respectiva é zero.

cen1 = int(input("Informe quantas moedas de 1 centavo possui: "))
cen5 = int(input("Informe quantas moedas de 5 centavos possui: "))
cen10 = int(input("Informe quantas moedas de 10 centavos possui: "))
cen25 = int(input("Informe quantas moedas de 25 centavos possui: "))
cen50 = int(input("Informe quantas moedas de 50 centavos possui: "))
real1 = int(input("Informe quantas moedas de 1 real possui: "))

totalcen = (cen1 * 1) + (cen5 * 5) + (cen10 * 10) + (cen25 * 25) + (cen50 * 50) 

somatotal =  real1 + (totalcen / 100)

print("Você possui um total de", somatotal, "reais")