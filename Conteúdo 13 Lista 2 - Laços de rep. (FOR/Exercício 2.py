#Exercício 2
#Escrever um algoritmo que leia uma quantidade de números que deve ser lidos e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50], [51,75] e [76,100].

vlr = int(input("quantos números devem ser lidos: "))

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

for n in range (0,vlr):
    num = int(input("Informe quais números devem ser lidos: ")) 
    if 0 < num <= 25:
        intervalo1 += 1  
    elif 26 < num <= 50:
        intervalo2 += 1
    elif 51 < num <= 75:
        intervalo3 += 1   
    elif  76 < num <= 100:
        intervalo4 += 1    
    
print(f"No intervalo de 0 a 25 tem um total de {intervalo1} números")
print(f"No intervalo de 26 a 50 tem um total de {intervalo2} números")
print(f"No intervalo de 51 a 75 tem um total de {intervalo3} números")
print(f"No intervalo de 76 a 100 tem um total de {intervalo4} números")
