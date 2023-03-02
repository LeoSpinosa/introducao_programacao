#Exercício 2
#Solicite que o usuário preencha uma lista de 5 valores inteiro. Percorra a lista e verifique quantos valores são pares.

lista = []
par = 0

for n in range(0,5):
    valor = int(input(f"Informe o valor {n + 1}: "))
    lista.append(valor)

for a in lista:
    if a % 2 == 0:
        par += 1

print(lista)
print(par)
