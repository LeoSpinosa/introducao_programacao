#Exercício 1
#Converta as temperaturas da lista celsius = [0, 15, 40] para fahrenheit e adicione a lista fahrenheit = [ ].
#calculo = celsius * (9/5) + 32

celsius = [0, 15, 40]
fahrenheit = []

for n in range (0, len(celsius)):
    temp = celsius[n] * (9/5) + 32
    fahrenheit.append(temp)
    
print(fahrenheit)

#----------------------------------------------

celsius = [0, 15, 40]
fahrenheit = []

for n in range (0, len(celsius)):
    n = n * (9/5) + 32
    fahrenheit.append(n)
    
print(fahrenheit)


#----------------------------------------------

c = [0, 15, 40]
f = []

for n, t in enumerate(c):
    novat: t * (9/5) + 32
    f.append(novat)

print(f)
