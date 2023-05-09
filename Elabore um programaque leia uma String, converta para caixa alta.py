string = input("Entre com uma String: ").upper()
caracteres = {}

for c in string:
    if c in caracteres:
        caracteres[c] += 1
    else:
        caracteres[c] = 1

for c in caracteres:
    if caracteres[c] == 1:
        print("O caractere", c, "aparece 1 vez")
    else:
        print("O caractere", c, "aparece", caracteres[c], "vezes")