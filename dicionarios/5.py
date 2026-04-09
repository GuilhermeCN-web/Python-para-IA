lista1 = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5
}

lista2 = {
    0: 6,
    1: 7,
    2: 8,
    3: 9,
    4: 10
}

lista3 = {}

# Copiando lista1
for i in lista1:
    lista3[i] = lista1[i]

# Copiando lista2 (ajustando índices)
for i in lista2:
    lista3[len(lista1) + i] = lista2[i]

print("Lista 3:", lista3)