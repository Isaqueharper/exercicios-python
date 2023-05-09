num = input("Digite um número inteiro com três algarismos: ")


if len(num) != 3:
    print("O número digitado não possui três algarismos.")
else:
    
    inverso = num[::-1]

    soma = int(num) + int(inverso)

    
    print("O inverso do número é:", inverso)
    print("A soma é:", num, "+", inverso, "=", soma)