#Exercício 3
#Tendo como dados de entrada:
#● A altura 
#● E o sexo de uma pessoa (‘M’ masculino e ‘F’ feminino)
#Construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#● Para homens: (72.7*h)-58
#● Para mulheres: (62.1*h)-44.7

altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo, M para masculino e F para feminino: ")
homem = (72.7*altura)-58
mulher = (62.1*altura)-44.7

if sexo == "M":
     print("Seu peso ideal é de: %.2f"%(homem))
else:
    print("Seu peso ideal é de: %.2f"%(mulher))
