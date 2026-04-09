notas = {
    0: 7.5,
    1: 8.0,
    2: 6.5,
    3: 9.0
}

soma = 0

for i in notas:
    print("Nota:", notas[i])
    soma += notas[i]

media = soma / len(notas)

print("Média:", media)