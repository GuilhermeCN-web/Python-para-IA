def somaImposto(taxaImposto, custo):
    custo += custo * (taxaImposto / 100)
    return custo

print(somaImposto(10, 100))