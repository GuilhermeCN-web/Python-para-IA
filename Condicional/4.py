valor_casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos para pagar: "))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print(f"Prestação mensal: R$ {prestacao:.2f}")

if prestacao <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")