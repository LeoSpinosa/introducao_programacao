#Exercício 3
#Escreva um algoritmo para ler o número total de eleitores de um município,
#onúmero de votos brancos, nulos e válidos.
#Calcular e escrever o percentual quecada um representa em relação ao total de eleitores.

eleitor = int(input("Total de eleitores: "))
votobranco = int(input("Votos em branco: "))
votonulo = int(input("Votos nulos: "))
votovalido = int(input("Votos válidos: "))

if eleitor > votobranco + votonulo + votovalido or eleitor < votobranco + votonulo +votovalido:
    print("Valores inválidos")
else:
    print ("Quantidade de votos em branco é de: %.0f por cento"%((votobranco * 100) / eleitor))
    print ("Quantidade de votos nulos é de: %.0f por cento"%((votonulo * 100) / eleitor))
    print ("Quantidade de votos válidos é de: %.0f por cento"%((votovalido * 100) / eleitor))