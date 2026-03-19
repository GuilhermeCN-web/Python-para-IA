def classe_eleitoral(idade):
    if idade < 16:
        return "Não-eleitor"
    elif 18 <= idade <= 65:
        return "Eleitor obrigatório"
    else:
        return "Eleitor facultativo"

print(classe_eleitoral(17))
print(classe_eleitoral(30))
print(classe_eleitoral(70))