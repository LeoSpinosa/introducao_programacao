#Exercício 2
#1.Solicite que o usuário informe o primeiro valor.
#2.Solicite que o usuário informe o segundo valor.
#3.Apresente a soma, subtração, multiplicação e o resto da divisão.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

soma = valor1 + valor2
print("soma", soma)

subtracao = valor1 - valor2
print("subtração", subtracao) 

multiplicacao = valor1 * valor2
print("multiplicação", multiplicacao)

divisao = int(valor1 / valor2)
print("divisão", divisao)

mod = valor1 % valor2
print("resto da divisão", mod)