#Exercício 8 
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Informe um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

frase1 = "Esse valor em centímetros é de {} e em melimetros {}".format(centimetros, milimetros)
print(frase1)