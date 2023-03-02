#Exercício 4
#Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura e sexo (0=masc, 1=fem) das pessoas.
#Faça um programa que leia 50 dados diferentes e informe:

#a) A maior e a menor altura encontradas;
#b) A média de altura das mulheres;
#c) A média de altura da população;
#d) O percentual de homens na população.

alt = 0
altmaior = 0
altmenor = 0
mediafem = 0
fem = 0
populacao = 0
mediapop = 0
masc = 0

for n in range (1,3):
    sexo = int(input("Informe o seu sexo, 0 pra masculino e 1 pra feminino: "))
    alt = float(input("Informe a sua altura em metros: "))

    if n == 1:
        altmenor = alt
        altmaior = alt

    if alt > altmaior:
        altmaior = alt

    elif alt < altmenor:
        altmenor = alt
    
    if sexo == 1:
        fem += 1
        mediafem += alt

    if sexo == 0 or sexo == 1:
        populacao += 1
        mediapop += alt

    if sexo == 0:
        masc += 1
    
percentual = masc * 100 / populacao 


print(f"\nA maior altura dentre as digitadas foi de: {altmaior}m, e a menor é de {altmenor}m")
print(f"A média de altura feminina é de: {mediafem / fem}m")        
print(f"A média de altura da populção é de: {mediapop / populacao}")
print(f"O percentual de homens na população é de: {percentual}%")
