caracteres = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
    5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'
}

consoantes = 0

for i in caracteres:
    if caracteres[i] not in 'aeiou':
        consoantes += 1

print("Caracteres:", caracteres.values())
print("Quantidade de consoantes:", consoantes)