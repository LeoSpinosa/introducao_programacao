#Exercício 5
#O usuário deverá informar:
#● Qual tabuada deseja
#● Em qual valor inicia
#● Em qual valor termina

#E o código deve retornar a tabuada, conforme a faixa informada.

num = int(input("Informe de tabuada que você deseja: "))
vlrinicial = int(input("Informe onde se deve iniciar: "))
vlrfinal = int(input("Informe onde se deve terminar: "))
 

for item in range(vlrinicial,vlrfinal + 1):
     print(f"{num} x {item} = {item * num}")