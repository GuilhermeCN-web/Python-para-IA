kwh = float(input("Quantidade de kWh consumidos: "))
tipo = input("Tipo de instalação (R - Residencial, C - Comercial, I - Industrial): ").upper()

if tipo == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65

elif tipo == "C":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60

elif tipo == "I":
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60

else:
    print("Tipo de instalação inválido.")
    preco = None

if preco is not None:
    print(f"Valor a pagar: R$ {preco:.2f}")