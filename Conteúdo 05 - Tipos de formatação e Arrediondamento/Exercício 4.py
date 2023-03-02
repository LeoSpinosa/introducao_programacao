#Exercício 4 
#Faça um progama que leia algo pelo teclado e mostre na tela o seu
#tipo primitivo e todas as informações possíveis sobre ele.

n = input("Informe um caractere para saber seu tipo: ")

print("O tipo dessa caractere é:", {type(n)})
print("Só tem espaços?", n.isspace())
print("É um número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfanumérico?", n.isalnum())
print("Está em maiúsculas?", n.isupper())
print("Está em minúsculas?", n.islower())
print("Está capitalizada", n.istitle())