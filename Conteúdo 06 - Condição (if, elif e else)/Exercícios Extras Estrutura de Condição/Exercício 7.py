#Exercício 7
#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe um segundo valor: "))
num3 = int(input("Informe um terceiro valor: "))


if num2 > num1 < num3:
    print(num1)
elif num1 > num2 < num3:
    print(num2)
else:
    print(num3)


if num2 < num1 > num3:
    print(num1)
elif num1 < num2 > num3:
    print(num2)
else:
    print(num3)