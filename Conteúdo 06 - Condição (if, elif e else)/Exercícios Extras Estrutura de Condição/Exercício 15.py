#Exercício 15
#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Informe o valor do primeiro lado: "))
lado2 = float(input("Informe o valor do segundo lado: "))
lado3 = float(input("Informe o valor do terceiro lado: "))

if lado1 + lado2 > lado3 != 0:
    print("Triângulo")
elif lado1 + lado3 > lado2 != 0:
    print("Triângulo")
elif lado2 + lado3 > lado1 != 0:
    print("Triângulo")
else:
    print("Não é um triângulo")

if lado1 == lado2 == lado3 != 0:
    print("Equilátero")
elif lado1 == lado2 != 0:
    print("Isósceles")
elif lado1 == lado3 != 0:
    print("Isósceles")
elif lado2 == lado3 != 0:
    print("Isósceles")
elif lado1 != lado2 != lado3 != 0:
    print("Escaleno")