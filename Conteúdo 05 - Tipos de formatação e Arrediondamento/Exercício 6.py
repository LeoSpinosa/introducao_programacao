#Exercício 6
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Insira um número: "))

vezes2 = numero * 2
vezes3 = numero * 3
raiz = numero ** (1/2)

frase1 = ("O dobro equivale a {}, o triplo a {} e a raiz quadrada a {}").format(vezes2, vezes3, raiz)
print(frase1)