palavra = input("Digite uma palavra: ")


palavra = palavra.lower().replace(" ", "")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")