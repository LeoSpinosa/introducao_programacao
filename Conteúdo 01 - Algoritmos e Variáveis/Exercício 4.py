#Exercício 4
#A  padaria  Hotpão  vende  uma  certa  quantidade  de  pães  franceses e  uma quantidade de broas a cada dia.
#Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50.
#Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos)
#e quanto deve guardar numa conta de poupança (10% do total arrecadado).
#Você foi contratado para fazer os cálculos para o dono.

pao = int(input("Informe a quantidade de pães vendidos: "))
broa = int(input("Informe a quantidade de broas vendidas: "))

multpao = pao * 0.12
multbroa = broa * 1.5

lucro = multpao + multbroa 
print("arrecadou ao final do dia", lucro, "reais")

poupanca = lucro * 0.1 
print("deve guardar",  poupanca, "em sua poupança")