import math , os
os.system('cls')

nome = input("Qual é o seu nome? ")

hora = int(input("Que horas são? (apenas a hora, sem os minutos) "))


if hora >= 6 and hora < 12:
    periodo = "Bom dia"
elif hora >= 12 and hora < 18:
    periodo = "Boa tarde"
else:
    periodo = "Boa noite"


print(f"{periodo}, {nome}!")
