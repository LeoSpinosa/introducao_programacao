#Exercício 5
#Um usuário deseja um algoritmo onde possa escolher que tipo de média deseja calcular a partir de 3 notas.
#Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média.
#● Aritmética
#● Ponderada (3,3,4)

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informa a terceira nota: "))
tipomedia = input("Informe o tipo de cálculo de média você deseja, A para aritmética e P para ponderada: ")


if tipomedia == "A":
    aritmetica = (nota1 + nota2 + nota3) / 3
    print("Sua média aritmética é de %.1f"%(aritmetica)) 
else:
    ponderada = (((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10)
    print("Sua média ponderada é de %.1f"%(ponderada))