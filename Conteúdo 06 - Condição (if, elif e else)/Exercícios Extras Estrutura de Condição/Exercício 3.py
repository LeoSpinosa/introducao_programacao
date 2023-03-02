#Exercício 3
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Informe seu sexo, F para Feminino e M para Masculino: ")

if letra == "F":
    print("Sexo feminino")
elif letra == "M":
    print("Sexo Masculino")
else:
    print("Sexo inválido")