#Exercício 5
#Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos.
#Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:

#a) 1,2,3,4 = voto para os respectivos candidatos;
#b) 5 = voto em branco;
#c) Outro valor = Voto nulo;
#d) Elabore um algoritmo que leia o código do candidado em um voto.

#Calcule e escreva:

#e) Total de votos para cada candidato;
#f) Total de votos nulos;
#g) Total de votos em branco.

#Faça um algoritmo para ler pelo menos 100 votos.

votocanditado1 = 0
votocantidato2 = 0
votocantidato3 = 0
votocantidato4 = 0
votonulo = 0 
votobranco = 0


for n in range(1,101):
    voto = int(input("Informe o seu voto (de 1 a 5): "))
    if voto == 1:
        votocanditado1 += 1
    elif voto == 2:
        votocantidato2 += 1
    elif voto == 3:
        votocantidato3 += 1
    elif voto == 4:
        votocantidato4 += 1
    elif voto == 5:
        votobranco += 1
    else:
        votonulo += 1


print(f"""\nPrimeiro canditado teve um total de {votocanditado1}  votos.
Segundo canditado teve um total de {votocantidato2}  votos.
Terceiro canditado teve um total de {votocantidato3}  votos.
Quarto canditado teve um total de {votocantidato4}  votos.
Teve um total de {votonulo}  votos nulos.
Teve um total de {votobranco}  votos em branco.\n""")