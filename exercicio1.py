import math , os
os.system('cls')

salario_fixo = float(input("Digite o salário fixo do funcionário: "))
valor_vendas = float(input("Digite o valor das vendas do funcionário: "))

comissao = 0.04 * valor_vendas
salario_final = salario_fixo + comissao

print("A comissão do funcionário é  R$ {:.2f}".format(comissao))
print("O salário final do funcionario é R$ {:.2f}".format(salario_final))
