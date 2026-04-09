T = {
    0: 10,
    1: 8,
    2: 0,
    3: 1,
    4: 2,
    5: 5,
    6: 2,
    7: 4
}

temperaturas = list(T.values())

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print("Temperaturas de Mons")
print(f"Menor temperatura: {menor}°C")
print(f"Maior temperatura: {maior}°C")
print(f"Temperatura média: {media:.2f}°C\n")

print("Todas as temperaturas:")
for indice, temp in T.items():
    print(f"Dia {indice}: {temp}°C")