#Exercício 4
#Escreva um programa que converta um intervalo de tempo dado em minutos,em horas, minutos e segundos.
#Por exemplo, se o tempo dado for 145,87minutos, o programa deve fornecer 2 h 25 min 52,2 s.

tempo = float(input("Informe uma quantidade de tempo em minutos: "))

horas = int((tempo // 60))
minutos = int((tempo % 60))
segundos = int((tempo % 1) * 60)

print (horas, "horas", minutos, "minutos", segundos, "segundos")