#Exercício 2
#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta.

while True:

    lista = []
    media = 0

    nome = str(input("Informe o nome do atleta: ")).strip()
    if nome == "":
        break
    else:
        lista.append(nome)
    
    for n in range(0, 5):
        salto = float(input(f"Informe a distância do salto {n + 1}: "))
        media += salto
        lista.append(salto)
    
    print(f"\nAtleta: {lista[0]}")
    print(f"Saltos: {lista[1:]}")
    print("Média de saltos: %.2f\n"%(media / 5))

    lista.clear()
    continue






