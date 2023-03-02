#Exercício 9
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe o segundo valor:  "))
num3 = int(input("Informe o terceiro valor: "))


if num2 < num1 > num3:
    print(num1)
elif num1 < num2 > num3:
    print(num2)
else:
    print(num3)



if num2 < num1 < num3:
    print(num1)
elif num1 < num2 < num3:
    print(num2)
elif num1 < num3 < num2:
    print(num3)



if num2 > num1 < num3:
    print(num1)
elif num1 > num2 < num3:
    print(num2)
elif num1 > num3 < num2: 
    print(num3)