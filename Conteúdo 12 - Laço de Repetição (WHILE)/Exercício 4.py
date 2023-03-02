#Exercício 4
#O usuário deverá informar qual tabuada deseja. E o código deve retornar a tabuada.

vlr = int(input("informe um valor para saber sua tabuada: "))
tabuada = 1

while tabuada <= 10:
    print(f"{tabuada} x {vlr} = {tabuada * vlr}")
    tabuada += 1