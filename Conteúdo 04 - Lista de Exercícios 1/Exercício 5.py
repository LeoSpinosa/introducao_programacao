#Exercício 5
#Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
#a) o novo peso se a pessoa engordar 15% sobre o peso digitado;
#b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input("informe seu peso: "))

engordou = peso * 0.15
emagreceu = peso * 0.2

totalengordou = peso + engordou 

totalemagreceu = peso - emagreceu 

print("Engordou: ", totalengordou, "quilos.")
print("Emagreceu: ", totalemagreceu, "quilos.")