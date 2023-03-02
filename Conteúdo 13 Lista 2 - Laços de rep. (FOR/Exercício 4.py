#Exercício 4
#Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 3centímetros por ano.
#Construir um algoritmo que calcule e imprima quantos anos serão necessários para que Juca seja maior que Chico.

chico = 1.5
juca = 1.1
crescimentochico = 0.02
crescimentojuca = 0.03
ano = 0

while juca <= chico:
    juca += crescimentojuca
    chico += crescimentochico
    ano += 1
print(f"Juca precissará de {ano} anos para ser maior que Chico.")