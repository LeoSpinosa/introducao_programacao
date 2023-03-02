#Exercício 11
#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

area = largura * altura
tinta = area / 2

frase1 = "A área da parede é de {}m² e são necessários {}L de tinta para pinta-la".format(area, tinta)
print(frase1)
