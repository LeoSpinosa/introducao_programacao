#Exercício 6
#Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento em grãos de trigo da seguinte maneira:
#Os grãos de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro tivesse um grão
#e as casas seguintes o dobro da anterior. Construa um algoritmo que calcule quantos grãos de trigo a Rainha deverá pagar ao monge. Um tabuleiro tem 64 casas.

tabuleiro = 64
casa = 1

for n in range(1, 64):
    casa *= 2
    
print(casa)