#Exercício 1
#Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
#● infantil A = 5 - 7 anos
#● infantil B = 8-10 anos
#● juvenil A = 11-13 anos
#● juvenil B = 14-17 anos
#● adulto = maiores de 18 anos

idade = int(input("Informe sua idade: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10: 
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Adulto"
else:
    categoria = "Inválido"

print("Sua categoria correspondente a sua idade é: {}".format(categoria))
