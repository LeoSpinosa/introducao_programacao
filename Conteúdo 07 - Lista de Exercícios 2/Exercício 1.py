#Exercício 1
#Escrever um algoritmo que lê o número de identificação, 
#as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios quefazem parte da avaliação.
#Calcular a média de aproveitamento, usandoa fórmula: MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7
#A atribuição de conceitos obedece a tabela abaixo: 


#Média de Aproveitamento                Conceito
#      9,0                                 A
#  7,5 e < 9,0                             B
#  6,0 e < 7,5                             C
#  4,0 e < 6,0                             D
#    < 4,0                                 E

#O algoritmo deve escrever o número do aluno, suas notas, a média dosexercícios, a média de aproveitamento,
#o conceito correspondente e amensagem: APROVADO se o conceito for A,B ou C e REPROVADO seo conceito for D ou E.


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))


me = (nota1 + nota2 + nota3) / 3

ma = (nota1 + (nota2 * 2) + (nota3 * 3) + me ) / 7

if 9 <= ma <= 10:
    conceito = "A"
elif 7.5 <= ma < 9:
    conceito = "B"
elif 6 <= ma < 7.5:
    conceito = "E"
elif 4 <= ma < 6:
    conceito = "D"
elif 0 < ma < 4:
    conceito = "E"


if conceito == "A":
    situacao = "Aprovado"
elif conceito == "B":
    situacao = "Aprovado"
elif conceito == "C":
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Primeira nota: ", nota1)
print("Segunda nota: ", nota2)
print("Média: %.1f"%(ma))
print("Média Exercícios: %.1f"%(me))
print("Conceito: ", conceito)
print("Situação: ", situacao)

print("FIM")