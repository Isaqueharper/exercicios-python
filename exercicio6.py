import math , os
os.system('cls')

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

if media >= 9.0:
    print('A, aprovado.')
elif media > 7.5:
    print('B, aprovado.')
elif media > 6.0:
    print('C, aprovado.')
elif media > 4.0:
    print('D, reprovdo.')
else:  
    print('E, reprovado.')
    
print(f' a media do aluno é:', media)