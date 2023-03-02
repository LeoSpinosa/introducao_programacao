#Exercício 2
#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:"São múltiplos" ou "Não são múltiplos".

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe um segundo valor: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")