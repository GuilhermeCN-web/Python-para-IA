km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))

preco = (dias * 60) + (km * 0.15)

print(f"Preço total a pagar: R$ {preco:.2f}")