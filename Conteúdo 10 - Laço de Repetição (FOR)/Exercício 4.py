#Exercício 4
#O usuário deverá informar qual tabuada deseja. E o código deve retornar a tabuada.

num = int(input("Informe de que número você deseja ver a tabuada do 1 ao 10: "))

for item in range(1,11):
     print(f"{num} x {item} = {item * num}")