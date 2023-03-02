#Exercício 5
#Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório.
#Suponha que os números digitados são um intervalo crescente.
#Exemplo:

#-Limite inferior: 3
#-Limite superior: 12
#-Saída: 4 6 8 10
#-Soma: 28

inf = int(input("Informe o limite inferior: "))
sup = int(input("Informe o limite superior: "))
pares = 0

for n in range (inf,sup):
    if n % 2 == 0:
        print(n)
        pares += n

print(f"A soma dos números pares nesse intervalo é de: {pares}")