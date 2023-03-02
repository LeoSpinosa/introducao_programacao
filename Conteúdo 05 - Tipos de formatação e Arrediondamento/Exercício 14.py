#Exercício 14
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Informe a temperatura em celsius: "))

fahrenheit = (celsius * 1.8) + 32

frase1 = ("Essa temperatura em celcius é equivalente a %.1f graus fahrenheit")%(fahrenheit)
print(frase1)