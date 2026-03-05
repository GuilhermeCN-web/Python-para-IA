salario = float(input("Digite o salário atual: "))
porcentagem = float(input("Digite a porcentagem de aumento (%): "))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)