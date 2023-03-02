#Exercício 3
#Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço 
#sabendo-se que este sofreu um desconto de 10%. 

precoproduto = int(input("Informe o preço do produto: "))

desconto = precoproduto * 0.1

total = precoproduto - desconto 

print("Preço total é de: ", total)