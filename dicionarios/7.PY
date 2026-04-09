V = {
    0: 9,
    1: 8,
    2: 7,
    3: 12,
    4: 0,
    5: 13,
    6: 21
}

P = {}
I = {}

for indice, numero in V.items():
    if numero % 2 == 0:
        P[indice] = numero
    else:
        I[indice] = numero

print("Separação Pares e Ímpares")
print("Lista Original:")
for i, v in V.items():
    print(f"  {i}: {v}")

print("\nPares (P):")
for i, v in P.items():
    print(f"  {i}: {v}")

print("\nÍmpares (I):")
for i, v in I.items():
    print(f"  {i}: {v}")