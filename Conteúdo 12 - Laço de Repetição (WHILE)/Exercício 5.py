#Exercício 5
#O usuário deverá informar:
#● Qual tabuada deseja
#● Em qual valor inicia
#● Em qual valor termina

#E o código deve retornar a tabuada, conforme a faixa informada.

tabuada = int(input("Informe qual tabuada deseja: "))
vlrinicial = int(input("Informe qual o valor inical: "))
vlrfinal = int(input("Informe o valor final: "))

while vlrinicial <= vlrfinal:
    print(f"{tabuada} x {vlrinicial} = {tabuada * vlrinicial}")
    vlrinicial += 1