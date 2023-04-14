import math , os
os.system('cls')

# Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe as opções de operações para o usuário
print("Escolha uma operação:")
print("1 - Média entre os números digitados")
print("2 - Diferença entre o maior e o menor número digitado")
print("3 - Produto entre os números digitados")
print("4 - Divisão do primeiro pelo segundo")


opcao = int(input("Digite o número da operação desejada: "))


if opcao == 1:
    media = (num1 + num2) / 2
    print(f"A média entre {num1} e {num2} é {media}.")
elif opcao == 2:
    if num1 > num2:
        diferenca = num1 - num2
    else:
        diferenca = num2 - num1
    print(f"A diferença entre {num1} e {num2} é {diferenca}.")
elif opcao == 3:
    produto = num1 * num2
    print(f"O produto entre {num1} e {num2} é {produto}.")
elif opcao == 4:
    if num2 == 0:
        print("Não é possível dividir por zero.")
    else:
        divisao = num1 / num2
        print(f"A divisão de {num1} por {num2} é {divisao}.")
else:
    print("Opção inválida. Escolha uma operação de 1 a 4.")
