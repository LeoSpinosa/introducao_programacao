'''

Variáveis

É um espaço na memória, que serve para armazenar um determinado valor.
Cada espaço na memória é associado a um identificador - palavra utilizada na declaração da variável.

●Iniciar com letra.
●Sem espaços.
●Sem acentos.
●Sem carácter especial, mas pode conter _.


Operações Aritméticas

valor1 = 10
valor2 = 20

soma = valor1 + 30
subtracao = valor2 - valor1
multiplicacao = 100 * 2
divisao = valor2 / 3
divisaoExata = valor1 // 3
resto = 30 % valor2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão Exata: {divisaoExata}")
print(f"Resto: {resto}")


Operadores Relacionais

Cada saída resultará em um TRUE ou um FALSE.


Operadores Booleanos

●AND: Só será verdadeiro se todos forem verdadeiro.
●OR: Basta um ser verdadeiro para atender.


Estrutura Condicional

●Sempre iniciará com IF
●Pode conter vários ELIF para o mesmo IF
●Pode conter apenas um ELSE para o mesmo IF
●ELIF e ELSE são opcionais.


Exercício

1.Considerando:

b1 = False
b2 = True
b3 = True

Qual a(s) saída(s)?
R: S2, S4, S5

if (b1 == True):

    print ("S1")

else:

    if (b2 == True):

        if(b3 == True):

            print ("S2")

        else:

            print ("S3")



    print ("S4")



print ("S5")      


2.É possível que apenas a saída s5 seja apresentada? Caso sim, informe quais os valores lógicos de b1, b2, b3?
R: Não é possível.

'''